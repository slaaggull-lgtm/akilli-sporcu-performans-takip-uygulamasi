# Akıllı Sporcu Performans Takip Uygulaması - Mimari Tasarım Dokümanı

Bu doküman, uygulamanın iOS (Swift) ve Android (Kotlin/Java) platformlarında kullanılacak olan modüler mimarisini tanımlar.

## 1. Mimari Yaklaşım: Clean Architecture + MVVM
Uygulama, sürdürülebilirlik ve test edilebilirlik için **Clean Architecture** prensiplerini ve **MVVM (Model-View-ViewModel)** tasarım desenini benimser.

### Katmanlar:
1. **Data Layer (Veri Katmanı):**
   - **Remote Data Source:** Retrofit (Android) / URLSession-Alamofire (iOS) ile REST API iletişimi.
   - **Local Data Source:** Room (Android) / CoreData-Realm (iOS) ile yerel önbellekleme.
   - **Repository Implementation:** Verinin nereden (bulut veya yerel) alınacağına karar veren mantık.

2. **Domain Layer (İş Mantığı Katmanı):**
   - **Entities:** Uygulamanın temel veri modelleri (User, Workout, Metrics).
   - **Use Cases:** Tek bir işi yapan sınıflar (örn: `CalculateVO2Max`, `GetUserWorkouts`). Bu katman platformdan bağımsızdır.

3. **Presentation Layer (Arayüz Katmanı):**
   - **View:** UI bileşenleri (Compose/XML - Android, SwiftUI - iOS).
   - **ViewModel:** View'dan gelen olayları işler ve Use Case üzerinden veriyi getirerek UI durumunu (State) günceller.

---

## 2. Ekranlar ve Navigasyon Yapısı
Uygulama, bir **Bottom Navigation Bar** üzerine kurulu 4 ana ekrandan oluşur:

1. **Dashboard (Ana Ekran):** Günlük özet veriler (kalp atışı, adımlar, mevcut hedef).
2. **Workouts (Antrenman Ekranı):** Aktif spor takibi, kronometre ve anlık sensör verileri.
3. **Analytics (Analiz Ekranı):** Haftalık grafikler, performans skorları ve gelişim trendleri.
4. **Profile (Profil Ekranı):** Kullanıcı bilgileri, cihaz ayarları (Bluetooth BLE) ve hedefler.

---

## 3. REST API ve İletişim Planı
- **Protokol:** HTTPS üzerinde JSON tabanlı RESTful API.
- **Kimlik Doğrulama:** Firebase Auth / JWT Bearer Token.
- **İletişim Stratejisi:**
  - Tüm istekler asenkron (Coroutines/Combine) yürütülür.
  - **Offline-First:** Veriler önce yerelde gösterilir, arka planda güncellenir.
  - **Hata Yönetimi:** İnternet yoksa veya API hatası alınırsa yerel veritabanı referans alınır.

## 4. Teknoloji Stack Önerisi
| Özellik | Android | iOS |
| :--- | :--- | :--- |
| Dil | Kotlin | Swift |
| UI | Jetpack Compose | SwiftUI |
| Veritabanı | Room | CoreData / Realm |
| Networking | Retrofit | URLSession / Alamofire |
| DI | Hilt / Koin | Swinject / Factory |
| Asenkron | Coroutines & Flow | Combine / Async-Await |
