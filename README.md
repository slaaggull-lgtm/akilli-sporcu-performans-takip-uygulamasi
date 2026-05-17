# Akıllı Sporcu Performans Takip Uygulaması

Bu proje; giyilebilir sensörlerden (akıllı saat, fitness takip cihazları vb.) elde edilen anlık biyometrik ve kinematik verileri toplayıp analiz ederek, sporcuların performansını değerlendiren, sakatlanma risklerini minimize eden ve kişiselleştirilmiş dinamik antrenman önerileri sunan hibrit ve yapay zeka destekli bir mobil uygulama platformudur.

---

## 🚀 Proje Özellikleri

- **Gerçek Zamanlı Sensör Entegrasyonu:** Apple HealthKit, Google Fit ve Bluetooth LE (BLE) protokolleri üzerinden akıllı saatler ve giyilebilir cihazlarla kesintisiz senkronizasyon (Nabız, Kadans, Adım, SpO2).
- **Yapay Zeka Destekli Koşu Analitiği:** Koşu performansını değerlendiren Python tabanlı analitik motor, VO2 Max tahmini, antrenman yoğunluk analizi ve egzersiz stres skoru (TSS) hesaplama.
- **On-Device Machine Learning:** TensorFlow Lite (.tflite) tabanlı yapay sinir ağları ile cihaz üzerinde gecikmesiz performans skoru tahmini.
- **Dinamik Antrenman Planlayıcı:** Kullanıcının geçmiş spor deneyimi, BMI, nabız değişkenliği (HRV) ve anlık yorgunluk analizine göre periyodik olarak güncellenen esnek egzersiz programları.
- **Çevrimdışı Çalışma (Offline-First):** SQLite / Room veritabanı altyapısı sayesinde internet bağlantısı olmasa bile veri kaybı yaşamadan kesintisiz kayıt ve sonrasında asenkron bulut senkronizasyonu.
- **Gelişmiş Performans Optimizasyonu:** CPU, RAM ve GPU verimliliğini üst düzeye çıkaran, görsel önbellekleme (NSCache) ve arka plan işlemleri (Coroutines/Dispatchers) ile optimize edilmiş akıcı mobil deneyim.

---

## 🛠️ Teknoloji Yığını (Tech Stack)

### Mobil Platformlar
- **Android:** Kotlin, Jetpack Compose, XML, Room Persistence Library, Coroutines & Flow, Hilt DI.
- **iOS:** Swift, SwiftUI, Core Bluetooth, URLSession / Alamofire, Combine, NSCache.

### Yapay Zeka & Analitik (AI / Data Science)
- **Modelleme:** Python, TensorFlow / Keras, NumPy, Pandas, Scikit-learn.
- **Mobil Entegrasyon:** TensorFlow Lite (TFLite) Converter ve Interpreter API.

### Bulut Altyapısı (Backend / Backend-as-a-Service)
- **Kimlik Doğrulama:** Firebase Authentication (E-posta/Şifre doğrulama ve Session yönetimi).
- **Veritabanı ve Senkronizasyon:** Firebase Realtime Database / Firestore ve RESTful JSON API altyapısı.

---

## 🏗️ Sistem Mimarisi

Uygulama, sürdürülebilirlik, test edilebilirlik ve modülerlik hedefleri doğrultusunda **Clean Architecture** prensiplerini ve **MVVM (Model-View-ViewModel)** tasarım desenini temel alır.

```mermaid
graph TD
    subgraph Presentation Katmanı
        View[UI Views - SwiftUI/Compose] <--> ViewModel[ViewModels]
    end
    subgraph Domain Katmanı (Platform Bağımsız)
        ViewModel --> UseCases[Use Cases / Egzersiz Algoritmaları]
        UseCases --> Entities[Entities - User, Workout, Metrics]
    end
    subgraph Data Katmanı
        UseCases --> Repository[Repository Interface]
        RepositoryImpl[Repository Impl] -.-> Repository
        RepositoryImpl --> RemoteDS[Remote Data Source - Firebase/REST API]
        RepositoryImpl --> LocalDS[Local Data Source - Room/Realm]
    end
```

### Katman Açıklamaları
1. **Presentation Layer:** Kullanıcı arayüzünü (SwiftUI/Jetpack Compose) ve arayüz durumunu (UI State) yöneten View-ViewModel çiftlerini içerir.
2. **Domain Layer:** Uygulamanın en çekirdek iş mantığını içerir. Frameworklerden, kütüphanelerden ve platform bağımlılıklarından tamamen bağımsızdır.
3. **Data Layer:** Verinin yerel SQLite (Room) veritabanından mı yoksa bulut servislerinden (Firebase/REST API) mi alınacağına karar veren veri yönetim katmanıdır.

---

## 📊 Performans Analizi ve ML Modeli

Koşu analitiği algoritmaları `analytics/` dizini altında yer almaktadır:
- **`RunningAnalytics` (`analytics/running_analytics.py`):** Ham mesafe, süre, adım sayısı ve ortalama nabız verilerini işleyerek **Hız**, **Tempo**, **Kadans** ve **VO2 Max** (aerobik kapasite) değerlerini hesaplar.
- **`export_tflite.py`:** TensorFlow Keras katmanları ile eğitilen performans tahmin modelini `.tflite` formatına dönüştürür. `running_model.tflite` modeli mobil uygulamanın varlıkları (assets) içerisine eklenerek yerelde yüksek performansla çalıştırılır.

---

## 📁 Proje Dizin Yapısı

```
akilli-sporcu-performans-takip-uygulamasi/
├── analytics/                        # Python Performans Analitiği & ML Modelleri
│   ├── models/                       # Eğitilmiş TFLite modelleri
│   ├── tests/                        # Algoritma test senaryoları
│   ├── running_analytics.py          # Fizyolojik ve kinematik veri analizi
│   └── export_tflite.py              # TFLite model eğitim ve dönüştürme scripti
│
├── app/                              # Android Mobil Uygulama Kaynak Kodları (Room & Auth)
│   ├── build.gradle                  # Gradle bağımlılıkları ve SDK ayarları
│   └── src/main/java/com/sporcu/akillitakip/
│       └── data/
│           ├── local/                # Yerel Depolama (Room Entity, DAO, AppDatabase)
│           └── remote/               # Uzak Bağlantılar (Firebase AuthRepository)
│
├── docs/                             # Mimari ve Teknik Dokümantasyon
│   └── architecture/
│       └── architecture_design.md    # Katmanlı mimari ve API planlama detayları
│
├── README.md                         # Proje Tanıtımı ve Genel Kılavuz
└── projeakisi.md                     # Haftalık Geliştirme Süreci ve Görev Takip Akışı
```

---

## 👥 Geliştirme Ekibi ve Görev Dağılımı

| Geliştirici | Rol / Görev Alanı | Durum |
| :--- | :--- | :--- |
| **Sıla Ağgül** | Teknoloji Analizi, Antrenman Planlama Algoritması, API Mimarisi, Optimizasyon | ✅ Tamamlandı |
| **Nur Beyda Genç** | Proje Kapsamı & Analizi, Veri Toplama Gereksinimleri, Database Stratejisi | ✅ Tamamlandı |
| **Şevval Bulut** | Sistem Gereksinimleri, Performans ML Analizi, UI/UX Wireframe, Arayüz Testleri | ✅ Tamamlandı |
| **Baver Katar** | Geliştirme Ortamı Kurulumu, iOS & Android Mimari Tasarım, TFLite Koşu Analiz Algoritması, Room DB Entegrasyonu | ✅ Tamamlandı |
| **Asım Gökalp** | Bluetooth Sensör Araştırması, UI/UX Trend Analizi, iOS REST API & BLE Senkronizasyonu, Performans Optimizasyonları | ✅ Tamamlandı |
