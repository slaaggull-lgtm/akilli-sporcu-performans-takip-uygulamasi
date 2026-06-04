
### Akıllı Sporcu Performans Takip Uygulaması

*Gerçek zamanlı sensör verisi · AI destekli sakatlanma risk analizi · Kişiselleştirilmiş antrenman*

<br/>

[![Branches](https://img.shields.io/badge/Git%20Branches-13-informational?style=flat-square)](https://github.com)
[![Commits](https://img.shields.io/badge/Commits-208-brightgreen?style=flat-square)](https://github.com)
[![Files](https://img.shields.io/badge/Files-62-blue?style=flat-square)](https://github.com)
[![Folders](https://img.shields.io/badge/Folders-32-purple?style=flat-square)](https://github.com)
[![License](https://img.shields.io/badge/License-MIT-red?style=flat-square)](LICENSE)

</div>

---

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

---

## 🎯 Proje Hakkında

**Akıllı Sporcu Performans Takip Uygulaması**, sporcu performansını bütünsel olarak izleyen, yapay zeka destekli bir mobil sağlık ve fitness platformudur. Uygulama; Bluetooth sensörlerden elde edilen gerçek zamanlı biyometrik verilerle sakatlanma riskini tahmin eder, kişiselleştirilmiş antrenman planları önerir ve uzun vadeli performans trendlerini analiz eder.

```
Sporcular için bir antrenör, bir fizyoterapist ve bir veri analistinin
tek bir uygulamada birleşimi.
```

### 🏆 Temel Hedefler

| Hedef | Açıklama |
|-------|----------|
| 🔴 Sakatlanma Önleme | AI tabanlı gerçek zamanlı risk sınıflandırması |
| 📈 Performans Takibi | BLE sensörlerle anlık metrik izleme |
| 🧠 Akıllı Planlama | Kişiselleştirilmiş antrenman programı üretimi |
| 📱 Çoklu Platform | Native Android & iOS destek |
| 🔄 Offline-First | Bağlantısız ortamda tam işlevsellik |

---

## ✨ Özellikler

- **🩺 Sakatlanma Risk Analizi** — Makine öğrenimi modeli ile egzersiz sırasında gerçek zamanlı risk tahmini
- **📡 Bluetooth Sensör Entegrasyonu** — BLE protokolü üzerinden kalp hızı, ivmeölçer ve jiroskop verisi
- **🏋️ Antrenman Planı Üretici** — Kullanıcı profiline ve geçmiş verisine göre dinamik plan oluşturma
- **📊 Performans Analitiği** — Zaman serisi görselleştirme ve trend analizi
- **🔔 Akıllı Bildirimler** — FCM tabanlı proaktif uyarı ve hatırlatma sistemi
- **☁️ Bulut Senkronizasyonu** — Firebase ile cihazlar arası anlık veri senkronizasyonu
- **📤 Veri Dışa Aktarım** — CSV/JSON formatında veri export desteği

---

## 🏗 Sistem Mimarisi

```
┌─────────────────────────────────────────────────────────────────┐
│                     PRESENTATION LAYER                          │
│   ┌─────────────────────┐    ┌──────────────────────────┐      │
│   │  Android (Java/MVVM) │    │    iOS (Swift/SPM)        │      │
│   │  Room DB · BLE       │    │  BluetoothManager · Cache │      │
│   └──────────┬──────────┘    └────────────┬─────────────┘      │
└──────────────┼─────────────────────────────┼────────────────────┘
               │         REST API            │
┌──────────────▼─────────────────────────────▼────────────────────┐
│                      BACKEND LAYER                              │
│         Python Flask · JWT Auth · Docker Container              │
│   /routes/auth.py  /routes/workout.py  /export/                 │
└──────────────────────────────┬──────────────────────────────────┘
                               │
         ┌─────────────────────┼─────────────────────┐
         │                     │                     │
┌────────▼────────┐  ┌────────▼────────┐  ┌────────▼────────┐
│   AI / ML Layer  │  │  Firebase DB    │  │  Notification   │
│  TFLite Model   │  │  Realtime Sync  │  │  FCM Service    │
│  InjuryAnalyzer │  │  SQL + NoSQL    │  │  Scheduler      │
└─────────────────┘  └─────────────────┘  └─────────────────┘
```

> **Mimari Yaklaşım:** Katmanlı mimari (Layered Architecture) ile mikroservis ilkeleri birleştirilmiştir. İstemci tarafında MVVM deseni, sunucu tarafında servis bazlı modüler yapı uygulanmaktadır.

---

## 🛠 Teknoloji Yığını

<table>
<tr>
<th>Katman</th>
<th>Teknoloji</th>
<th>Amaç</th>
</tr>
<tr>
<td><b>Android</b></td>
<td>Java · Room ORM · Retrofit</td>
<td>Native Android istemci, MVVM</td>
</tr>
<tr>
<td><b>iOS</b></td>
<td>Swift · SPM · CoreBluetooth</td>
<td>Native iOS istemci</td>
</tr>
<tr>
<td><b>Backend</b></td>
<td>Python 3 · Flask · JWT</td>
<td>REST API sunucusu</td>
</tr>
<tr>
<td><b>AI/ML</b></td>
<td>TensorFlow Lite · Python</td>
<td>Sakatlanma riski modeli</td>
</tr>
<tr>
<td><b>Veritabanı</b></td>
<td>Firebase Realtime DB · SQL</td>
<td>Hibrit veri katmanı</td>
</tr>
<tr>
<td><b>Bildirim</b></td>
<td>Firebase FCM</td>
<td>Push bildirim servisi</td>
</tr>
<tr>
<td><b>DevOps</b></td>
<td>Docker · Git</td>
<td>Container & versiyon yönetimi</td>
</tr>
</table>

---

## 📁 Proje Yapısı

```
akillitakip/
├── 📂 ai/                          # Yapay Zeka Modülleri
│   ├── injury/
│   │   ├── InjuryRiskAnalyzer.py   # Sakatlanma risk sınıflandırıcısı
│   │   └── InjuryRiskTests.py      # Model testleri
│   ├── models/                     # Eğitilmiş model dosyaları
│   ├── running_analytics.py        # Koşu analitik motoru
│   ├── optimization.py             # Model optimizasyonu
│   └── export_tflite.py            # TFLite dönüştürücü
│
├── 📂 client/                      # İstemci Uygulamaları
│   ├── android/                    # Android (Java/MVVM)
│   │   └── app/src/main/java/com/akillitakip/
│   │       ├── data/local/         # Room DB katmanı
│   │       ├── data/remote/        # API iletişim katmanı
│   │       ├── domain/             # İş mantığı
│   │       └── presentation/       # UI state yönetimi
│   ├── ios/                        # iOS (Swift/SPM)
│   │   └── Sources/
│   │       ├── Bluetooth/          # BLE yönetimi
│   │       ├── Cache/              # Görsel önbellekleme
│   │       ├── Network/            # API servisleri
│   │       └── Performance/        # Performans monitörü
│   └── notifications/              # FCM bildirim sistemi
│
├── 📂 server/                      # Backend API
│   ├── routes/                     # API endpoint rotaları
│   ├── export/                     # Veri dışa aktarım servisi
│   └── app.py                      # Ana uygulama giriş noktası
│
├── 📂 database/                    # Veritabanı şemaları
│   ├── schema.sql                  # İlişkisel tablo tanımları
│   ├── firebase_structure.md       # NoSQL yapısı dokümantasyonu
│   └── database/seed_data.sql      # Test verileri
│
├── 📂 datasets/                    # Örnek veri setleri
├── 📂 docs/                        # Proje dokümantasyonu
├── 📂 config/                      # Uygulama yapılandırmaları
├── 📂 tests/                       # Otomatik test dosyaları
├── Dockerfile                      # Container yapılandırması
└── README.md
```

---

## 🚀 Kurulum

### Gereksinimler
- Python 3.9+
- Node.js 18+ (sadece geliştirme araçları için)
- Android Studio / Xcode
- Docker (opsiyonel, deployment için)

### Backend Kurulumu

```bash
# Repoyu klonlayın
git clone https://github.com/your-org/akillitakip.git
cd akillitakip

# Ortam değişkenlerini ayarlayın
cp .env.example .env

# Bağımlılıkları yükleyin
pip install -r server/requirements.txt

# Sunucuyu başlatın
python server/app.py
```

### Docker ile Kurulum

```bash
docker build -t akillitakip .
docker run -p 5000:5000 --env-file .env akillitakip
```

### AI Modül Kurulumu

```bash
pip install -r ai/requirements.txt
python ai/export_tflite.py
```

---

## 👥 Takım

<table>
<tr>
<td align="center" width="200">
<br/>
<b>Sıla Ağgül</b><br/>
<img src="https://img.shields.io/badge/Proje%20Lideri-1A56A8?style=for-the-badge" alt="Proje Lideri"/>
<br/><small>Koordinasyon · Planlama · Delivery Yönetimi</small>
</td>
<td align="center" width="200">
<br/>
<b>Baver Katar</b><br/>
<img src="https://img.shields.io/badge/Sistem%20Mimarı-6B21A8?style=for-the-badge" alt="Sistem Mimarı"/>
<br/><small>Mimari Tasarım · Entegrasyon · DevOps</small>
</td>
<td align="center" width="200">
<br/>
<b>Asım Gökalp</b><br/>
<img src="https://img.shields.io/badge/UI%2FUX%20Tasarımcı-D97706?style=for-the-badge" alt="UI/UX"/>
<br/><small>Figma · Kullanıcı Deneyimi · Prototip</small>
</td>
</tr>
<tr>
<td align="center" width="200">
<br/>
<b>Nur Beyda Genç</b><br/>
<img src="https://img.shields.io/badge/Veritabanı%20Sorumlusu-059669?style=for-the-badge" alt="DB"/>
<br/><small>Firebase · SQL · Veri Modelleme</small>
</td>
<td align="center" width="200">
<br/>
<b>Şevval Bulut</b><br/>
<img src="https://img.shields.io/badge/Backend%20Geliştirici-DC2626?style=for-the-badge" alt="Backend"/>
<br/><small>Python · Flask · REST API</small>
</td>
<td align="center" width="200">
<br/>
</td>
</tr>
</table>

---

## 📊 Proje İstatistikleri

| Metrik | Değer |
|--------|-------|
| 🌿 Aktif Branch | 13 |
| 💾 Toplam Commit | 208 |
| 📁 Klasör Sayısı | 32 |
| 📄 Dosya Sayısı | 62 |
| 🧪 Test Dosyaları | 2 |
| 📚 Dokümantasyon Dosyaları | 8 |

---

## 🔗 Bağlantılar

| Kaynak | Bağlantı |
|--------|----------|
| 📖 Dokümantasyon | [projeakisi.md](projeakisi.md)|
| 🚀 Deployment Kılavuzu | [`DEPLOYMENT_GUIDE.txt`](DEPLOYMENT_GUIDE.txt) |
| 🔒 Güvenlik Politikası | [`SECURITY.md`](SECURITY.md) |
| 🤝 Katkı Kılavuzu | [`CONTRIBUTING.md`](CONTRIBUTING.md) |

---

## 🤝 Katkıda Bulunma

Katkı sağlamak için lütfen [`CONTRIBUTING.md`](CONTRIBUTING.md) dosyasını inceleyin. Genel iş akışı:

1. Bir `feature/isim` veya `fix/isim` branch oluşturun
2. Değişikliklerinizi commit edin
3. Pull Request açın ve inceleme bekleyin

---

## 📄 Lisans

Bu proje [MIT Lisansı](LICENSE) kapsamında lisanslanmıştır.

---


