# Akıllı Sporcu Takip Uygulaması 

Profesyonel sporcu performans analiz paneli · AI destekli sakatlanma risk analizi · Gerçek zamanlı antrenman takibi

🌐 **Canlı Demo:** [akilli-sporcu-uyg.onrender.com](https://akilli-sporcu-uyg.onrender.com)

Branches · Commits · Files · Folders · License

## 📋 İçerik

- [Proje Hakkında](#-proje-hakkında)
- [Özellikler](#-özellikler)
- [Sistem Mimarisi](#-sistem-mimarisi)
- [Teknoloji Yığını](#-teknoloji-yığını)
- [Proje Yapısı](#-proje-yapısı)
- [Kurulum](#-kurulum)
- [Takım](#-takım)
- [Katkıda Bulunma](#-katkıda-bulunma)
- [Lisans](#-lisans)

## 🎯 Proje Hakkında

**AkıllıTakip Pro**, sporcuların antrenman verilerini (nabız, süre, kalori, algılanan yorgunluk) tek bir panelde toplayan, kural tabanlı bir yapay zeka motoruyla sakatlanma riskini analiz eden ve uzun vadeli performans trendlerini görselleştiren web tabanlı bir sporcu takip platformudur.

> Sporcular için bir antrenör, bir veri analisti ve bir sağlık danışmanının tek bir panelde birleşimi.

## 🏆 Temel Hedefler

| Hedef | Açıklama |
|---|---|
| 🔴 Aşırı Yüklenme Önleme | Kural tabanlı risk skorlama motoru ile erken uyarı |
| 📈 Performans Takibi | Antrenman bazlı BPM, süre, kalori ve yorgunluk metrikleri |
| 🧠 Akıllı Koçluk | Geçmiş verilere göre otomatik AI koç geri bildirimi |
| 👥 Çoklu Sporcu Yönetimi | Tek panelden birden fazla sporcu profili izleme |
| 📤 Raporlama | Tek tıkla resmi PDF performans raporu dışa aktarımı |

## ✨ Özellikler

- 📊 **4 Gelişmiş Grafik** — BPM/Risk trendi, Süre/Kalori dağılımı, Yorgunluk trendi, Aktivite türü dağılımı (7/30/90 gün ve tüm zamanlar filtreli)
- 🧠 **AI Koç & Risk Analiz Motoru** — Nabız, yorgunluk ve antrenman yoğunluğuna göre otomatik risk skoru ve gerekçeli geri bildirim
- 🎯 **Hedef Sistemi** — Haftalık/aylık süre, antrenman sayısı ve kalori hedefleri ile otomatik ilerleme takibi
- 🏅 **Başarım Sistemi** — Antrenman sayısı, toplam kalori ve dayanıklılık eşiklerine bağlı rozet kilidi açma
- 🔔 **Bildirim Merkezi** — Yeni antrenman, başarım ve risk uyarıları için canlı bildirim paneli
- 📤 **PDF Rapor** — BMI, risk skoru, başarımlar ve antrenman geçmişini içeren resmi rapor çıktısı
- 📅 **Aktivite Takvimi** — GitHub katkı haritası tarzı, son 35 günü gösteren yoğunluk matrisi
- 👥 **Çoklu Sporcu Yönetimi** — Sporcu ekleme, profil güncelleme ve silme
- 🌓 **Dark / Light Tema** — Tercih `localStorage` ile kalıcı olarak saklanır
- 📡 **Sensör Verisi Simülasyonu** — Gerçek sensör entegrasyonunu test etmek için rastgele veri üretimi


<img width="2937" height="1667" alt="Ekran Resmi 2026-06-27 23 26 34" src="https://github.com/user-attachments/assets/0e9dd464-ba8d-4fb0-8980-0a72a7ed4e60" />














<img width="2921" height="1672" alt="Ekran Resmi 2026-06-27 23 26 44" src="https://github.com/user-attachments/assets/c24f147a-7a70-4e72-99c7-0127b35bebb7" />









## 🏗 Sistem Mimarisi

```
┌─────────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                          │
│        Jinja2 Templates · Tailwind CSS · Chart.js               │
│   Ana Sayfa · Analiz · AI Koç · Takvim · Profil                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │  HTTP (Flask Routing)
┌──────────────────────────────▼──────────────────────────────────┐
│                      APPLICATION LAYER                          │
│              Python · Flask · Jinja2 · Gunicorn                 │
│   /training  /athlete  /chart-data  /export-pdf  /notifications │
└──────────────────────────────┬──────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
┌────────▼────────┐  ┌────────▼────────┐  ┌────────▼────────┐
│  AI / Risk Motoru│  │   Veri Katmanı  │  │  Bildirim       │
│  Kural tabanlı   │  │  SQLite ·       │  │  Servisi        │
│  risk skorlama   │  │  SQLAlchemy ORM │  │  (in-app)       │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

**Mimari Yaklaşım:** Katmanlı mimari (Layered Architecture) uygulanmıştır. Sunum katmanı (Jinja2 şablonları), uygulama/iş mantığı katmanı (Flask route'ları ve servis fonksiyonları) ve veri katmanı (SQLAlchemy ORM + SQLite) birbirinden ayrılmıştır; bu sayede her katman bağımsız olarak geliştirilip test edilebilir.

## 🛠 Teknoloji Yığını

| Katman | Teknoloji | Amaç |
|---|---|---|
| Backend | Python 3 · Flask | Sunucu tarafı uygulama ve route yönetimi |
| Şablon Motoru | Jinja2 | Sunucu taraflı dinamik HTML render |
| Frontend | Tailwind CSS · Font Awesome | Responsive, modern arayüz |
| Veri Görselleştirme | Chart.js | Çizgi, bar ve doughnut grafikler |
| Veritabanı | SQLite · Flask-SQLAlchemy | İlişkisel veri katmanı, ORM |
| AI / Risk Motoru | Kural tabanlı Python motoru | Sakatlanma riski skorlama |
| Deployment | Render.com · Gunicorn | Üretim ortamı barındırma |
| Versiyon Kontrol | Git & GitHub | Kaynak kod ve sürüm yönetimi |

## 📁 Proje Yapısı

```
akillitakip/
├── 📂 templates/                   # Jinja2 Şablonları
│   ├── base.html                   # Ortak layout (navbar, sidebar, tema)
│   ├── index.html                  # Ana Sayfa (özet kartlar)
│   ├── analytics.html              # Gelişmiş Analiz (4 grafik)
│   ├── ai_coach.html               # AI Analiz Odası (risk geçmişi)
│   ├── calendar.html               # Aktivite Takvimi
│   ├── profile.html                # Profil & Sağlık
│   └── pdf_template.html           # PDF rapor şablonu
│
├── 📂 static/                      # Statik dosyalar (görsel/varlık)
│
├── app.py                          # Ana uygulama: modeller, route'lar, AI motoru
├── requirements.txt                # Python bağımlılıkları
├── Procfile                        # Render/Heroku başlatma komutu
└── README.md
```

## 🚀 Kurulum

### Gereksinimler

- Python 3.9+
- pip

### Yerel Kurulum

```bash
# Repoyu klonlayın
git clone https://github.com/slaaggull-lgtm/akilli-sporcu-v3.git
cd akilli-sporcu-v3

# Bağımlılıkları yükleyin
pip install -r requirements.txt

# Uygulamayı başlatın
python app.py
```

Tarayıcıda `http://localhost:5000` adresine gidin.

### Üretim Ortamı (Render.com)

`Procfile` içeriği:

```
web: gunicorn app:app
```

Render.com üzerinde otomatik deployment için repo bağlanması yeterlidir; `requirements.txt` ve `Procfile` hazır şekilde repo içinde yer almaktadır.



## 👥 Takım

| Üye | Rol | Sorumluluk |
|---|---|---|
| **Sıla Ağgül** | Proje Lideri | Koordinasyon · Planlama · Delivery Yönetimi |
| **Baver Katar** | Sistem Mimarı | Mimari Tasarım · Entegrasyon · DevOps |
| **Asım Gökalp** | UI/UX | Tasarım · Kullanıcı Deneyimi · Prototip |
| **Nur Beyda Genç** | Veritabanı | SQLite/SQLAlchemy · Veri Modelleme |
| **Şevval Bulut** | Backend | Python · Flask · Route/Servis Geliştirme |

## 📊 Proje İstatistikleri

| Metrik | Değer |
|---|---|
| 🌿 Aktif Branch | 12 |
| 💾 Toplam Commit | 227 |
| 📁 Klasör Sayısı |8 |
| 📄 Dosya Sayısı |65 |


## 🔗 Bağlantılar

| Kaynak | Bağlantı |
|---|---|
| 🌐 Canlı Demo | https://akilli-sporcu-uyg.onrender.com |
| 📖 Dokümantasyon | README.md |

## 🤝 Katkıda Bulunma

Genel iş akışı:

1. Bir `feature/isim` veya `fix/isim` branch oluşturun
2. Değişikliklerinizi commit edin
3. Pull Request açın ve inceleme bekleyin

## 📄 Lisans

Bu proje MIT Lisansı kapsamında lisanslanmıştır.



