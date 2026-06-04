# ==============================================================================
# SMARTATHLETE PLATFORM - ENTERPRISE MULTI-STAGE DOCKER ARCHITECTURE
# ==============================================================================
# Bu dosya, Akıllı Sporcu Performans Takip Uygulaması'nın Python Analitik Motoru
# ve yapay zeka katmanını (MediaPipe/TFLite) izole bir konteynerde ayağa kaldırır.

# ------------------------------------------------------------------------------
# 1. AŞAMA: DERLEME VE BAĞIMLILIK HAZIRLAMA (Builder Stage)
# ------------------------------------------------------------------------------
FROM python:3.10-slim AS builder

LABEL maintainer="SmartAthlete Dev Team"
LABEL project="Akilli Sporcu Performans Takip Uygulamasi"

# Derleme için gerekli sistem araçlarının kurulması
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /build

# Tekerlek (Wheel) paketleri oluşturarak bağımlılıkların optimize edilmesi
COPY analytics/requirements.txt* ./
RUN pip install --upgrade pip && \
    if [ -f requirements.txt ]; then pip wheel --no-cache-dir --no-deps --wheel-dir /build/wheels -r requirements.txt; fi

# ------------------------------------------------------------------------------
# 2. AŞAMA: ÇALIŞMA VE ÜRETİM ORTAMI (Final Production Stage)
# ------------------------------------------------------------------------------
FROM python:3.10-slim AS final

# Python çalışma optimizasyonları (Gereksiz bytecode yazımını engeller, logları anlık basar)
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive
ENV APP_HOME=/home/app/web

WORKDIR $APP_HOME

# MediaPipe, OpenCV ve grafik işleme kütüphanelerinin native bağımlılıkları
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    libgomp1 \
    curl \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# İlk aşamada derlenen optimize paketlerin nihai imaja taşınması
COPY --from=builder /build/wheels /images/wheels
RUN pip install --no-cache /images/wheels/* && rm -rf /images/wheels

# Proje klasör yapısının katı kurallarla container içine map edilmesi
COPY config/ $APP_HOME/config/
COPY datasets/ $APP_HOME/datasets/
COPY analytics/ $APP_HOME/analytics/
COPY generate_sample_data.py $APP_HOME/

# Güvenlik Protokolü: Root (Kök) yetkili kullanıcı yerine kısıtlı sistem kullanıcısı tanımı
RUN useradd -U -m -s /bin/bash appuser && \
    chown -R appuser:appuser $APP_HOME
USER appuser

# Sunucu Sağlık Kontrolü (HEALTHCHECK): Konteynerin canlı olup olmadığını otomatik denetler
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
  CMD curl -f http://localhost:8080/health || exit 1

# Dış dünyaya açılan servis portu (REST API ve WebSocket trafiği için)
EXPOSE 8080

# Uygulamanın güvenli şekilde başlatılma komutu
ENTRYPOINT ["python"]
CMD ["generate_sample_data.py"]
