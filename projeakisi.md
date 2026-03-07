# Akıllı Sporcu Performans Takip Uygulaması - Proje Akışı

## Hafta 1

### Teknoloji Araştırması ve Seçimi
- Sorumlu: Sıla Ağgül
- Durum: Tamamlandı
- Yapılan:

Teknoloji Mimarisi, Yapay Zeka Entegrasyonu ve Sistem Altyapı Analizi

Native Mobil Geliştirme ve Donanım Entegrasyonu: Uygulamanın sporcu hareketlerini milisaniyelik gecikmelerle takip edebilmesi için hibrit çözümler (React Native/Flutter) yerine Native (Kotlin & Swift) dillerinin kullanımı üzerine derinlemesine analiz yapıldı. Cihazların İvmeölçer (Accelerometer), Jiroskop (Gyroskope) ve Barometre gibi donanımsal sensörlerinden gelen ham verilerin, uygulama katmanında en yüksek verimlilikle nasıl işleneceği teknik olarak raporlandı.

Gelişmiş Yapay Zeka (AI) ve Bilgisayarlı Görü (Computer Vision) Mimarisi: Antrenman sırasında sporcunun formunu (postürünü) analiz etmek için MediaPipe Pose Landmarker ve TensorFlow Lite modelleri incelendi. Kamera görüntüsü üzerinden 33 farklı eklem noktasının (skeletal tracking) koordinat düzleminde nasıl takip edileceği ve bu verilerin doğru/yanlış hareket analizi için hangi matematiksel modellerle karşılaştırılacağı üzerine bir altyapı tasarlandı.

Giyilebilir Cihaz Haberleşme Protokolleri: Apple Watch, Garmin ve Samsung Gear gibi giyilebilir cihazlarla kesintisiz veri aktarımı sağlamak amacıyla Core Bluetooth ve Android Bluetooth Low Energy (BLE) kütüphaneleri araştırıldı. Nabız değişkenliği (HRV) ve VO2 Max verilerinin HealthKit ve Google Fit SDK üzerinden asenkron olarak çekilip kullanıcı profiliyle eşleştirilmesi süreci planlandı.

Bulut Tabanlı Veri Mimarisi ve Backend Stratejisi: Binlerce kullanıcının anlık antrenman verilerini depolayabilmek için Firebase Firestore (NoSQL) veritabanı mimarisi kurgulandı. Veri güvenliği kapsamında GDPR ve KVKK uyumluluğu için veri şifreleme yöntemleri (AES-256) ve kullanıcı yetkilendirme (Firebase Auth/JWT) protokolleri sistem tasarımına dahil edildi.

Sistem Optimizasyonu ve Proje Yönetimi: Uygulamanın arka planda (background) çalışırken batarya tüketimini minimize edecek WorkManager ve Grand Central Dispatch (GCD) optimizasyonları üzerine çalışıldı. GitHub üzerinden ekip içi kod kalitesini korumak adına Branching (dal yönetimi) kuralları belirlendi ve projenin dokümantasyon standartları oluşturularak haftalık raporlama sistemi stabilize edildi.



### Proje Analizi ve Kapsam Tanımı
- Sorumlu: Nur Beyda Genç
- Durum: Devam Ediyor
- Yapılan:

### Gereksinim Toplama ve Belgeleme
- Sorumlu: Şevval Bulut
- Durum: Devam Ediyor
- Yapılan:

### Geliştirme Ortamı Kurulumu
- Sorumlu: Baver Katar
- Durum: Devam Ediyor
- Yapılan:

### Veri Toplama ve İşleme Altyapısı Araştırması
- Sorumlu: Asım Gökalp
- Durum: Devam Ediyor
- Yapılan:
