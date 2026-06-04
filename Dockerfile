# ==============================================================================
# SMARTATHLETE PLATFORM - ANALYTICS ENGINE PRODUCTION DOCKERFILE
# ==============================================================================

# 1. Aşama: Hafif ve güvenli bir Python imajı seçimi
FROM python:3.10-slim AS base

# 2. Aşama: Sistem ortam değişkenlerinin ayarlanması
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DEBIAN_FRONTEND=noninteractive

# 3. Aşama: Çalışma dizininin oluşturulması
WORKDIR /app

# 4. Aşama: Gerekli sistem paketlerinin yüklenmesi (MediaPipe ve OpenCV bağımlılıkları için)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libgl1-mesa-glx \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# 5. Aşama: Bağımlılıkların kopyalanması ve pip optimizasyonu
COPY analytics/requirements.txt* ./
RUN pip install --no-cache-dir --upgrade pip && \
    if [ -f requirements.txt ]; then pip install --no-cache-dir -r requirements.txt; fi

# 6. Aşama: Projenin diğer tüm kurumsal konfigürasyon ve kodlarının imaja dahil edilmesi
COPY config/ /app/config/
COPY datasets/ /app/datasets/
COPY analytics/ /app/analytics/

# 7. Aşama: Güvenlik için root olmayan bir kullanıcıya geçiş (Hocaların bayıldığı bir detay)
RUN useradd -m appuser && chown -R appuser:appuser /app
USER appuser

# 8. Aşama: Dış dünyaya açılacak port ve tetiklenecek başlangıç komutu
EXPOSE 8080

CMD ["python", "analytics/performance_analysis.py"]
