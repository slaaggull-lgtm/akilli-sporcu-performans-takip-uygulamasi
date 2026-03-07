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
- Durum: Tamamlandı
- Yapılan:

Giyilebilir Sensör Verilerinin Toplanması ve Donanım Entegrasyonu:
Akıllı saatler ve fitness takip cihazlarından elde edilen biyometrik ve aktivite verilerinin mobil uygulamaya aktarılabilmesi için Bluetooth Low Energy (BLE) iletişim altyapısı üzerine araştırma yapılmıştır. Apple Watch, Garmin ve Samsung Gear gibi cihazlarla veri alışverişi sağlayan iOS Core Bluetooth ve Android Bluetooth Low Energy API yapıları incelenmiştir. Kalp atış hızı (Heart Rate), adım sayısı, mesafe, yakılan kalori ve uyku verileri gibi temel sporcu performans verilerinin mobil uygulama tarafından gerçek zamanlı olarak nasıl alınabileceği analiz edilmiştir.

Sağlık Veri Platformları ve SDK Entegrasyonu:
Giyilebilir cihazlardan elde edilen sağlık verilerinin uygulama içerisinde kullanılabilmesi için Apple HealthKit ve Google Fit SDK altyapıları incelenmiştir. Bu platformlar üzerinden HRV (Heart Rate Variability), VO2 Max ve aktivite yoğunluğu gibi gelişmiş performans verilerinin nasıl çekileceği ve kullanıcı profili ile nasıl ilişkilendirileceği araştırılmıştır. Ayrıca veri erişim izinleri, kullanıcı gizliliği ve platform politikaları teknik olarak değerlendirilmiştir.

Veri Ön İşleme ve Zaman Serisi Analizi:
Sensörlerden elde edilen ham verilerin doğrudan analiz edilmesi yerine belirli veri işleme aşamalarından geçirilmesi gerektiği belirlenmiştir. Bu kapsamda veri temizleme, eksik veri kontrolü, zaman serisi düzenleme ve veri normalizasyonu gibi veri ön işleme yöntemleri araştırılmıştır. Ayrıca performans analiz algoritmalarında kullanılmak üzere ortalama, maksimum ve minimum değerlerin hesaplanması gibi temel istatistiksel işlemler incelenmiştir.

Mobil Yapay Zeka ve Performans Analizi Altyapısı:
Toplanan sporcu verilerinin mobil cihaz üzerinde analiz edilebilmesi için TensorFlow Lite tabanlı makine öğrenmesi modelleri incelenmiştir. Bu modeller sayesinde sporcu performans trendlerinin analiz edilmesi, yorgunluk seviyesinin tahmin edilmesi ve kullanıcıya kişiselleştirilmiş antrenman önerileri sunulabilmesi için bir veri analiz altyapısı planlanmıştır.

Veri Depolama Mimarisi ve Senkronizasyon Stratejisi:
Uygulamanın hem çevrimdışı hem de çevrimiçi çalışabilmesi için hibrit veri depolama yaklaşımı değerlendirilmiştir. Mobil cihaz üzerinde hızlı veri erişimi sağlamak amacıyla SQLite ve Realm veritabanı çözümleri incelenmiştir. Kullanıcı verilerinin uzun süreli saklanması ve cihazlar arası senkronizasyon için Firebase Firestore bulut veritabanı mimarisi araştırılmıştır.

API ve Veri İletişim Altyapısı:
Mobil uygulama ile backend servisleri arasındaki veri iletişimi için REST API mimarisi incelenmiştir. Sensör verilerinin JSON formatında sunucuya gönderilmesi ve analiz sonuçlarının mobil uygulamaya geri iletilmesi için API tabanlı veri akışı modeli tasarlanmıştır.
