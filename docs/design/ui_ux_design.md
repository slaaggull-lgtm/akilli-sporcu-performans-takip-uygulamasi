# Akıllı Sporcu Performans Takip Uygulaması - UI/UX Tasarım Dokümanı

Bu doküman; sporcuların antrenman ve fizyolojik verilerini kolayca izleyebilmesi, analizleri anlamlandırabilmesi ve antrenman önerileriyle sezgisel bir şekilde etkileşime girebilmesi amacıyla kurgulanan **UI/UX Arayüz Tasarım Standartlarını ve Platform Tasarım Yönergelerini** içerir.

---

## 🎨 1. Tasarım Sistemi (Design System)

Uygulamanın arayüz dili, premium spor markalarının estetiğiyle örtüşen, dinamik, enerjik ve odaklanmayı kolaylaştıran **modern karanlık mod (Dark Mode)** üzerine inşa edilmiştir.

### Renk Paleti (Color Palette)
- **Primary / Accent Neon Teal:** `#00F0FF` (Ana butonlar, vurgular, kalp ritmi dalgaları)
- **Secondary / Electric Blue:** `#007AFF` (Veri grafikleri, ikincil durumlar, navigasyon ikonları)
- **Performance / Glowing Green:** `#39FF14` (İyi performans, yüksek toparlanma hızı, VO2 Max skoru)
- **Intensity / Neon Purple:** `#BD00FF` (Yüksek yoğunluklu antrenman bölgeleri, özel bildirimler)
- **Background Black:** `#08080C` (Uygulamanın ana derin karanlık arka planı)
- **Card Background (Glassmorphism):** `rgba(255, 255, 255, 0.05)` ile `backdrop-filter: blur(20px)` (Kart bileşenleri ve modallar)

### Tipografi (Typography)
- **Başlıklar ve Önemli Metrikler:** **Outfit** (Sans-serif, yuvarlatılmış ve modern geometri, yüksek okunurluk sağlar)
- **Gövde Metinleri ve Etiketler:** **Inter** (Sans-serif, nötr, küçük boyutlarda bile yüksek kontrastlı okunurluk)

### İkonografi (Iconography)
- **iOS:** Apple **SF Symbols** kütüphanesi kullanılarak sistemle tam entegre, çizgi kalınlığı ayarlanabilir semboller.
- **Android:** Google **Material Symbols (Rounded/Outlined)** kütüphanesiyle Material Design 3 standartlarında tutarlılık.

---

## 📱 2. Temel Ekran Tasarımları ve İşlevleri

Uygulama, temel işlevlerini 4 ana ekran üzerinden **Bottom Navigation** (iOS'te Tab Bar) yapısı ile sunar.

### A. Ana Ekran (Dashboard Screen)
Kullanıcının o anki günlük performansını, aktiflik durumunu ve anlık biyometrik verilerini bir bakışta görebileceği merkezdir.
- **Üst Kısım:** Kullanıcı karşılama başlığı ("Merhaba Baver!") ve bugünkü motivasyon skoru.
- **Biyometrik Kartlar (Glassmorphism):**
  - **Kalp Ritmi Kartı:** Anlık nabız (BPM) ve nabız dalga grafiği (Teal neon çizgi).
  - **Kalori Kartı:** Yakılan aktif kalori (kcal) ve dairesel ilerleme halkası.
  - **Aktif Süre Kartı:** Yapılan antrenman süresi (dakika) ve kalan hedefler.
- **Haftalık Aktivite Grafiği:** Günlük yakılan kalori ve tamamlanan antrenmanların dikey bar grafik şeklinde gösterimi.

### B. Performans Göstergeleri Ekranı (Performance Analytics)
Sensör verilerinden üretilen derinlemesine fizyolojik analizleri görselleştirir.
- **VO2 Max Göstergesi:** Ekranın merkezinde yer alan, performans düzeyini (Örn: "54.5 - Mükemmel") ve aerobik kapasite sınıfını gösteren büyük dairesel neon gösterge.
- **Nabız Bölgeleri Dağılımı:** Antrenmanlar sırasında geçirilen sürelerin nabız bölgelerine (Aerobik, Anaerobik, VO2 Max, Yağ Yakımı) göre yatay bar grafik gösterimi.
- **Toparlanma ve Uyku Skoru:** Sporcunun bir sonraki antrenmana ne kadar hazır olduğunu gösteren "Recovery Rate" kartları.

### C. Antrenman Planları Ekranı (Workout Plans)
Kişiselleştirilmiş antrenman programlarının yönetildiği ve yeni egzersizlerin başlatıldığı ekrandır.
- **Haftalık Takvim:** Sporcunun o haftaki antrenman günlerini ve dinlenme günlerini gösteren kaydırılabilir yatay takvim bileşeni.
- **Dinamik Öneri Kartı:** Yapay zeka motorunun o günkü yorgunluk ve toparlanma durumuna göre önerdiği antrenman türü (Örn: "Bugün 45 dk. Hafif Tempo Koşu Öneriliyor").
- **Antrenman Başlat Butonu:** Hızlı ve kolay etkileşim için ekranın alt-orta kısmında konumlandırılmış, göze çarpan "Antrenmanı Başlat" aksiyon butonu.

### D. Kullanıcı Profili Ekranı (User Profile)
Kişisel ayarların, fiziksel parametrelerin ve entegrasyonların yönetildiği bölümdür.
- **Fiziksel Kartlar:** Yaş, boy, kilo, BMI ve egzersiz düzeyi gibi Room DB'de saklanan kullanıcı verilerinin şık bir grid yapısında sunumu.
- **Sensör & Sağlık Bağlantıları:** Apple HealthKit veya Google Fit bağlantı durumunu gösteren switch (açma/kapama) bileşenleri.
- **Ayarlar ve Geri Bildirim:** Uygulama genel ayarları ve doğrudan geliştirici ekibe iletilecek geri bildirim kanalı.

---

## 🎨 3. Platformlar Arası Tutarlılık Stratejisi (Cross-Platform)

Uygulamanın hem iOS hem de Android cihazlarda yerel (native) hissettirmesi, ancak marka kimliğini koruması için aşağıdaki kurallar uygulanmıştır:

| Arayüz Elemanı | iOS (SwiftUI) Standartları | Android (Compose / MD3) Standartları |
| :--- | :--- | :--- |
| **Navigasyon** | Alt kısımda saydam `UITabBar` yapısı, SF Symbols ikonları. | Alt kısımda Material Design 3 `NavigationBar`, Material Icons. |
| **Geri Bildirimler** | Haptic Engine (Taptic SDK) ile hafif fiziksel titreşimler. | Android Haptic Feedback sistemi ile dokunsal bildirimler. |
| **Yazı Tipi Modeli** | `Outfit` (Başlıklar) ve `San Francisco (SF Pro)` (Gövde). | `Outfit` (Başlıklar) ve `Roboto / Inter` (Gövde). |
| **Yükleniyor (Loading)** | `ProgressView` (Dönen çark standardı). | `CircularProgressIndicator` (MD3 animasyonu). |
| **Geri Butonu** | Sol üst köşede "Geri" metinsiz, sadece sol ok işareti. | Sol üst köşede standart Material geri oku. |

---

## 📈 4. Kullanıcı Geri Bildirim Döngüsü (Feedback Loop)

Kullanıcıların arayüzle ve antrenmanlarla olan deneyimini ölçmek, makine öğrenmesi algoritmalarını optimize etmek amacıyla **iki aşamalı bir geri bildirim mekanizması** tasarlanmıştır.

### A. Egzersiz Sonrası RPE Değerlendirmesi (Post-Workout Survey)
Her antrenman oturumu sonlandırıldığında otomatik olarak açılan, sporcunun antrenman zorluğunu değerlendirdiği ekrandır:
- **Borg RPE Ölçeği (Rate of Perceived Exertion):** Sporcudan antrenmanın zorluğunu 1 (Çok Kolay) ile 10 (Maksimum Efor) arasında puanlaması istenir.
- **Duygu Durum Seçicisi:** Antrenman sonrasındaki fiziksel hissi (Yorgun, Enerjik, Ağrılı, Harika) belirten minimalist emojiler.
- **Veri Akışı:** Bu veriler Room veritabanındaki `Workout` tablosunda güncellenir ve Firebase Firestore ile senkronize edilerek yapay zeka modelinin bir sonraki antrenman önerisini optimize etmesi için girdi (Input) olarak kullanılır.

### B. Uygulama İçi Arayüz ve Deneyim Anketi (In-App NPS/CSAT)
Arayüzün kullanım kolaylığını ölçmek için belirli aralıklarla tetiklenen mikro-anket mekanizması:
- **Mikro Geri Bildirim Butonu:** Kullanıcı Profili ekranında sürekli aktif olan "Deneyimi Puanla" butonu.
- **Unobtrusive Modal:** Antrenman dışındaki zamanlarda, kullanıcının işini bölmeyecek şekilde ekrana gelen tek soruluk, yıldızlı memnuniyet anketi.
- **Sürekli İyileştirme:** Toplanan veriler doğrudan Firebase analytics üzerinden UX ekibine raporlanır ve ısı haritaları (Heatmaps) ile birleştirilerek arayüz güncellemelerine yön verir.

---

## 🖼️ 5. Arayüz Ekran Görüntüleri ve Mockup'lar

Uygulamanın estetik vizyonunu, cam efekti (glassmorphism) detaylarını ve neon renk paletini gösteren premium mobil arayüz tasarımları aşağıda sunulmuştur:

````carousel
![Ana Ekran Dashboard Mockup](file:///c:/Users/Bağver/Desktop/ymt/akilli-sporcu-performans-takip-uygulamasi-main/akilli-sporcu-performans-takip-uygulamasi-main/docs/design/images/athlete_dashboard_mockup.png)
Ana Ekran (Dashboard) Mockup - Neon Teal vurgular, anlık nabız grafiği, kalori halkası ve haftalık aktivite barları.
<!-- slide -->
![Performans Analiz Ekranı Mockup](file:///c:/Users/Bağver/Desktop/ymt/akilli-sporcu-performans-takip-uygulamasi-main/akilli-sporcu-performans-takip-uygulamasi-main/docs/design/images/athlete_analytics_mockup.png)
Performans Göstergeleri (Analytics) Mockup - Dairesel VO2 Max göstergesi, uyku kalitesi ve toparlanma analiz grafikleri.
````

---

### 🚀 Geliştirme Takımı İçin Not
Arayüz bileşenlerinin kodlama aşamasında Android için `Compose Box / Card` yapılarına `blur(20.dp)` ve `border(1.dp, Color.White.copy(alpha = 0.1f))` verilerek cam efekti sağlanmalıdır. iOS tarafında ise SwiftUI `VisualEffectMaterial` veya `.background(.ultraThinMaterial)` kullanılarak arka plan derinliği native olarak elde edilecektir.
