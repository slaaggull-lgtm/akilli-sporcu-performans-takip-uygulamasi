# Akıllı Sporcu Performans Takip Uygulaması - Proje Akışı

## Hafta 1

### Teknoloji Araştırması ve Seçimi
- Sorumlu: Sıla Ağgül
- Durum: Tamamlandı
- Yapılan:

Teknoloji Mimarisi, Yapay Zeka Entegrasyonu ve Sistem Altyapı Analizi

Native Mobil Geliştirme ve Donanım Entegrasyonu: Uygulamanın sporcu hareketlerini milisaniyelik gecikmelerle takip edebilmesi için hibrit çözümler (React Native/Flutter) yerine Native (Kotlin & Swift) dillerinin kullanımı üzerine derinlemesine analiz yapıldı. Cihazların İvmeölçer (Accelerometer), Jiroskop (Gyroskope) ve Barometre gibi donanımsal sensörlerinden gelen ham verilerin uygulama katmanında en yüksek verimlilikle nasıl işleneceği teknik olarak raporlandı.

Gelişmiş Yapay Zeka (AI) ve Bilgisayarlı Görü (Computer Vision) Mimarisi: Antrenman sırasında sporcunun formunu (postürünü) analiz etmek için MediaPipe Pose Landmarker ve TensorFlow Lite modelleri incelendi. Kamera görüntüsü üzerinden 33 farklı eklem noktasının (skeletal tracking) koordinat düzleminde nasıl takip edileceği ve bu verilerin doğru/yanlış hareket analizi için hangi matematiksel modellerle karşılaştırılacağı üzerine bir altyapı tasarlandı.

Giyilebilir Cihaz Haberleşme Protokolleri: Apple Watch, Garmin ve Samsung Gear gibi giyilebilir cihazlarla kesintisiz veri aktarımı sağlamak amacıyla Core Bluetooth ve Android Bluetooth Low Energy (BLE) kütüphaneleri araştırıldı. Nabız değişkenliği (HRV) ve VO2 Max verilerinin HealthKit ve Google Fit SDK üzerinden asenkron olarak çekilip kullanıcı profiliyle eşleştirilmesi süreci planlandı.

Bulut Tabanlı Veri Mimarisi ve Backend Stratejisi: Binlerce kullanıcının anlık antrenman verilerini depolayabilmek için Firebase Firestore (NoSQL) veritabanı mimarisi kurgulandı. Veri güvenliği kapsamında GDPR ve KVKK uyumluluğu için veri şifreleme yöntemleri (AES-256) ve kullanıcı yetkilendirme (Firebase Auth/JWT) protokolleri sistem tasarımına dahil edildi.

Sistem Optimizasyonu ve Proje Yönetimi: Uygulamanın arka planda (background) çalışırken batarya tüketimini minimize edecek WorkManager ve Grand Central Dispatch (GCD) optimizasyonları üzerine çalışıldı. GitHub üzerinden ekip içi kod kalitesini korumak adına Branching (dal yönetimi) kuralları belirlendi ve projenin dokümantasyon standartları oluşturularak haftalık raporlama sistemi stabilize edildi.



### Proje Analizi ve Kapsam Tanımı
- Sorumlu: Nur Beyda Genç
- Durum: Tamamlandı
- Yapılan:

Proje Analizi: Giyilebilir Sensör Destekli Performans ve Sağlık Takip Sistemi

Bu doküman, projenin temel hedeflerini, kapsamını ve başarı kriterlerini detaylandırmak amacıyla hazırlanmıştır.

 Projenin Genel Hedefleri

- Performans Optimizasyonu: Sporculardan alınan nabız, uyku kalitesi ve hareket verilerini analiz ederek en verimli antrenman saatlerini ve yoğunluğunu belirlemek.
- Sakatlık Önleme (Injury Prevention): Aşırı yüklenme (overtraining) sinyallerini erkenden tespit edip kullanıcıyı uyarmak.
- Veri Görselleştirme: Karmaşık sensör verilerini, sporcunun kolayca anlayabileceği anlamlı grafiklere dönüştürmek.

 Kapsam (Scope)

- Veri Kaynakları: Apple Health, Google Fit ve Garmin gibi platformlardan gelen ham verilerin entegrasyonu.
- Analiz Motoru: Yapay zeka destekli, kişiselleştirilmiş antrenman öneri algoritması.
- Mobil Arayüz: Kullanıcı dostu dashboard, günlük raporlar ve anlık bildirim sistemi.
- Geri Bildirim Döngüsü: Sporcunun gelişimine göre dinamik olarak güncellenen haftalık programlar.

Çözülen Sorunlar ve Kullanıcı İhtiyaçları

Sorunlar:

- "Körlemesine" Antrenman: Sporcuların kendi vücut kapasitelerini bilmeden aşırı yüklenmesi.
- Veri Kirliliği: Akıllı saatlerin çok veri üretmesi ama bu verilerin ne anlama geldiğinin kullanıcı tarafından bilinmemesi.
- Standart Programlar: Herkes için aynı olan, kişiye özel olmayan genel geçer programların yetersizliği.

İhtiyaçlar:

- "Bugün ne kadar zorlamalıyım?" sorusuna bilimsel bir cevap.
- Yorgunluk ve toparlanma (recovery) sürelerinin net takibi.
- Sakatlık riskini minimize eden proaktif uyarılar.

 Başarı Kriterleri (KPIs)

- Hata Payı: Sensör verilerinin analizinde %90 ve üzeri tutarlılık.
- Kullanıcı Bağlılığı: Aktif kullanıcıların haftada en az 5 kez uygulamayı kontrol etmesi.
- Sakatlık Oranı: Uygulama önerilerine uyan kullanıcıların sakatlanma oranında (teorik olarak) %25 azalma.
- Performans Artışı: Kullanıcıların hedeflerine ulaşma süresinde %15 iyileşme.


### Gereksinim Toplama ve Belgeleme
- Sorumlu: Şevval Bulut
- Durum: Tamamlandı
- Yapılan:
Gereksinim Toplama ve Belgeleme
1. Proje Tanımı

Akıllı Sporcu Performans Takip Uygulaması, giyilebilir sensörlerden (akıllı saatler ve fitness takip cihazları) elde edilen verileri analiz ederek sporcuların performansını değerlendiren bir mobil uygulamadır.

Bu uygulama, kullanıcının fiziksel aktivitelerini izleyerek kişiselleştirilmiş antrenman önerileri sunmayı amaçlar. Ayrıca sporcuların performans gelişimini takip etmelerine ve sakatlanma risklerini azaltmalarına yardımcı olur.

2. Sistem Amaçları

Sporcu performansını veri tabanlı analiz etmek

Kullanıcının antrenman verilerini kayıt altına almak

Kişiselleştirilmiş antrenman planları oluşturmak

Sporcuların gelişimini grafiklerle göstermek

Sakatlanma riskini azaltmaya yardımcı olmak

3. Paydaşlar (Stakeholders)

Paydaş                                             	Rol

Sporcu:	                           Uygulamayı kullanarak performansını takip eder

Antrenör:                            Sporcu verilerini analiz ederek antrenman planı oluşturabilir

Uygulama Geliştiricileri:             Mobil uygulamayı geliştirir

Sistem Yöneticisi:                     Veri güvenliği ve sistem yönetimini sağlar
4. Fonksiyonel Gereksinimler (Functional Requirements)
FR1 – Kullanıcı Kaydı:

Kullanıcı uygulamaya kayıt olabilir.

Kullanıcı giriş yapabilir.

FR2 – Sensör Bağlantısı:

Uygulama Bluetooth LE ile giyilebilir cihazlara bağlanabilmelidir.

Akıllı saat veya fitness cihazından veri alınabilmelidir.

FR3 – Veri Toplama:

Uygulama aşağıdaki verileri toplayabilmelidir:

Kalp atış hızı

Adım sayısı

Yakılan kalori

Uyku verileri

Egzersiz süresi

FR4 – Veri Senkronizasyonu:

Sensör verileri mobil uygulama ile senkronize edilmelidir.

Veriler Firebase veritabanına kaydedilmelidir.

FR5 – Performans Analizi:

Toplanan veriler analiz edilmelidir.

Kullanıcıya performans değerlendirmesi sunulmalıdır.

Örnek analizler:

Haftalık performans grafiği

Ortalama kalp atış hızı

Aktivite yoğunluğu

FR6 – Antrenman Planı Oluşturma:

Uygulama kullanıcı verilerine göre:

Günlük antrenman planı oluşturur

Haftalık antrenman programı önerir

FR7 – Bildirim Sistemi:

Uygulama kullanıcıya şu bildirimleri gönderebilir:

Antrenman  hatırlatma

Günlük hedef tamamlandı bildirimi

5. Fonksiyonel Olmayan Gereksinimler (Non-Functional Requirements)
Performans:

Uygulama sensör verilerini gerçek zamanlı işleyebilmelidir.

Güvenlik

Kullanıcı verileri güvenli şekilde saklanmalıdır.

Firebase Authentication kullanılmalıdır.

Kullanılabilirlik

Kullanıcı arayüzü basit ve anlaşılır olmalıdır.

Uygulama yeni kullanıcılar için kolay kullanılabilir olmalıdır.

Uygulama aşağıdaki platformlarda çalışmalıdır:

iOS

Android

Veri Yönetimi

Veriler Realm veya SQLite veritabanında saklanmalıdır.

6. Kullanıcı Hikayeleri (User Stories):
Kullanıcı Hikayesi 1:

Bir sporcu olarak, günlük aktivitelerimi takip etmek istiyorum ki performansımı görebileyim.

Kullanıcı Hikayesi 2:

Bir sporcu olarak, akıllı saatimi uygulamaya bağlamak istiyorum ki antrenman verilerim otomatik olarak kaydedilsin.

Kullanıcı Hikayesi 3:

Bir sporcu olarak, performans analizimi görmek istiyorum ki gelişimimi takip edebileyim.

Kullanıcı Hikayesi 4:

Bir sporcu olarak, bana özel antrenman planı almak istiyorum ki daha verimli antrenman yapabileyim.

Kullanıcı Hikayesi 5:

Bir sporcu olarak, antrenman hatırlatmaları almak istiyorum ki antrenmanlarımı aksatmayayım.

7. Kullanılacak Teknolojiler:

Swift / Kotlin → Mobil uygulama geliştirme

Firebase → Veri saklama ve kullanıcı yönetimi

TensorFlow Lite → Performans analiz algoritmaları

Bluetooth LE → Giyilebilir cihaz bağlantısı

Realm / SQLite → Yerel veri depolama

9. Sistem Modülleri:

1-Veri Toplama Modülü:

Sensör verilerini toplar

Bluetooth bağlantısını yönetir

2-Veri Senkronizasyon Modülü:

Verileri Firebase'e gönderir

Offline verileri senkronize eder

3-Performans Analiz Modülü:

Kullanıcı verilerini analiz eder

Grafik ve rapor üretir

4- Antrenman Planı Modülü:

Kullanıcı performansına göre öneriler üretir

5-Kullanıcı Arayüzü:

Kullanıcı dostu tasarım

Grafikler ve performans ekranları

9. Beklenen Çıktılar

Sensör verilerini toplayan mobil uygulama

Performans analiz sistemi

Kişiselleştirilmiş antrenman planı oluşturucu

iOS ve Android mobil uygulaması

Test edilmiş kullanıcı arayüzü

### Geliştirme Ortamı Kurulumu
- Sorumlu: Baver Katar
- Durum: Tamamlandı
- Yapılan:

Mobil Uygulama İskeletinin Oluşturulması ve Platform Yapılandırması:
Uygulamanın hem iOS hem de Android platformlarında sorunsuz çalışabilmesi için gerekli altyapı kurulumları gerçekleştirilmiştir. Geliştirme ortamı yapılandırılarak projenin temel paket dizinleri, konfigürasyon dosyaları ve platformlara özgü SDK (Software Development Kit) entegrasyonları tamamlanmıştır.

Versiyon Kontrol Sistemi ve Dal (Branch) Yönetimi:
Proje kaynak kodlarının güvenli bir şekilde saklanması ve ekip içi eşzamanlı geliştirme sürecinin yönetilebilmesi amacıyla GitHub üzerinde versiyon kontrol altyapısı kurulmuştur. Kod çakışmalarını önlemek adına Git Branching modeli benimsenmiş; ana sürüm ve geliştirme dalları oluşturulmuştur. Ayrıca gereksiz sistem dosyalarının repoya yüklenmesini engellemek için yapılandırmalar sağlanmıştır.

Bağımlılık (Dependency) Yönetimi ve Kütüphane Entegrasyonu:
İlerleyen aşamalarda kullanılacak olan makine öğrenmesi (TensorFlow Lite), bulut veritabanı (Firebase) ve donanım haberleşme (BLE) araçlarının projeye dahil edilebilmesi için paket yöneticisi altyapıları (Android için Gradle, iOS için CocoaPods) kurulmuştur. Gerekli kütüphanelerin temel versiyon tanımlamaları yapılarak proje bağımlılıkları stabilize edilmiştir.

Lokal Geliştirme Ortamı ve Ekip Senkronizasyonu:
Takım üyelerinin projeyi kendi lokal ortamlarında hatasız bir şekilde ayağa kaldırabilmeleri için gerekli ortam değişkenleri (environment variables) ve derleme yapılandırmaları ayarlanmıştır. Geliştirici ortamlarının standartlaştırılması amacıyla gerekli dokümantasyonlar ve kurulum adımları hazırlanarak ekibe sunulmuştur.

  


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




## Hafta 2

### API Tasarımı
- Sorumlu: Sıla Ağgül
- Durum: Tamamlandı
- Yapılan:

API Mimarisi, Veri Akışı ve Sistem Entegrasyonu Tasarımı

Genel API Yaklaşımı: Mobil uygulama ile sunucu arasında güvenli, hızlı ve ölçeklenebilir bir veri iletişimi sağlamak amacıyla REST mimarisi temel alınarak API tasarımı yapılmıştır. Bu yapı, mobil uygulamanın farklı platformlarda (iOS ve Android) sorunsuz çalışabilmesini, verilerin hatasız iletilmesini ve veri bütünlüğünün korunmasını garanti altına alır. API tasarımında veri formatı olarak JSON tercih edilmiş, böylece hem insan tarafından okunabilir hem de sistemler arası uyumluluk sağlanmıştır.

Kullanıcı Yönetimi Endpointleri: Uygulamanın temel kullanıcı işlevlerini gerçekleştirebilmesi için kimlik doğrulama, kullanıcı kaydı, giriş ve profil yönetimi için detaylı endpointler tasarlanmıştır. Bu endpointler, veri güvenliği ve kullanıcı deneyimi açısından optimize edilmiştir:
- POST /register → Yeni kullanıcı kaydı; kullanıcı adı, e-posta ve şifre bilgileri güvenli bir şekilde sunucuya iletilir. Sistemde mevcut kullanıcılarla çakışma kontrolü yapılır ve başarılı kayıt sonrası kullanıcıya token üretilir.
- POST /login → Kullanıcı giriş işlemi; sağlanan kimlik bilgileri doğrulanır, JWT tabanlı token üretilir ve kullanıcıya güvenli bir oturum sağlanır. Giriş başarısız olduğunda anlamlı hata mesajları döndürülür.
- GET /user → Kullanıcı profil bilgilerini getirme; kullanıcıya ait isim, yaş, kayıt tarihi, son antrenman verileri ve genel istatistikler sunulur. Yetkilendirme mekanizması sayesinde yalnızca kendi verilerine erişim sağlanır.

Sporcu Verisi ve Antrenman Endpointleri: Sporcuların performans verilerini yönetmek için endpointler aşağıdaki şekilde tasarlanmıştır:
- GET /workoutData → Kullanıcının geçmiş antrenman verileri detaylı bir şekilde getirilir. Her veri; tarih, süre, kalp atışı, adım sayısı, yakılan kalori ve aktivite tipi gibi bilgilerle birlikte döndürülür. Bu sayede kullanıcı kendi performansını takip edebilir ve gelişim eğrilerini görebilir.
- POST /workoutData → Yeni antrenman verisi ekleme işlemi; mobil uygulamadan alınan veriler sunucuya güvenli bir şekilde iletilir ve veritabanına kaydedilir. Veri doğrulama, eksik veya hatalı veri kontrolleri ve zaman damgası ekleme işlemleri bu endpoint üzerinden yapılır.

Sensör Veri Entegrasyonu: Giyilebilir cihazlardan gelen sensör verilerinin doğru ve güvenli bir şekilde sunucuya iletilmesi için özel endpointler oluşturulmuştur:
- POST /sensorData → Kalp atışı, adım sayısı, yakılan kalori, VO2 Max ve diğer biyometrik veriler bu endpoint aracılığıyla sunucuya gönderilir. API, verilerin zaman damgalı ve sıralı bir şekilde kaydedilmesini sağlayarak veri bütünlüğünü garanti eder. Ayrıca yüksek frekansta veri akışı olması durumunda verilerin önbellekleme ve toplu işleme yöntemleri ile işlenmesi planlanmıştır.

Veri Güvenliği ve Yetkilendirme: API tasarımında güvenlik öncelikli olarak ele alınmıştır. Kullanıcı doğrulama işlemleri JWT tabanlı token sistemi ile yapılır. API, yetkisiz erişim girişimlerini engellemek için kullanıcı ve token bazlı kontrol mekanizmalarına sahiptir. Ayrıca hassas kullanıcı verilerinin şifrelenerek saklanması (AES-256 veya benzeri protokoller) önerilmiş ve GDPR ile KVKK uyumluluğu açısından değerlendirilmiştir.

Performans Optimizasyonu ve Ölçeklenebilirlik: API endpointlerinin yüksek veri hacmi altında sorunsuz çalışabilmesi için performans ve ölçeklenebilirlik kriterleri planlanmıştır. GET ve POST isteklerinin asenkron çalışması, yük dengeleme (load balancing) stratejileri ve cache mekanizmaları ile verilerin hızlı erişimi sağlanacaktır. Bu sayede binlerce kullanıcı aynı anda veri gönderse bile sistem yanıt süreleri düşmeyecektir.

Dokümantasyon ve Test Süreci: Tüm API endpointleri için OpenAPI/Swagger tabanlı kapsamlı dokümantasyon hazırlanması planlanmıştır. Bu dokümantasyon ile her endpointin amacı, parametreleri, beklenen veri formatları ve hata kodları detaylı bir şekilde açıklanır. Mobil uygulama geliştiricileri, backend ekibi ve test uzmanları bu dokümantasyon sayesinde API’yi doğru ve hatasız bir şekilde entegre edebilir. Test süreçlerinde birim testler (unit test) ve entegrasyon testleri uygulanarak API’nin güvenilirliği ve tutarlılığı sağlanacaktır.

Gelecek Planlaması ve Geliştirilebilirlik: API tasarımı esnek ve modüler bir yapıya sahiptir. Yeni endpoint eklenmesi, mevcut verilerin genişletilmesi veya üçüncü taraf hizmetlerle entegrasyon gerektiğinde minimal değişiklik ile uygulanabilir. Bu sayede projenin ilerleyen aşamalarında kullanıcı taleplerine veya teknolojik yeniliklere hızlı adaptasyon sağlanabilecektir.

### UI/UX Wireframe Tasarımı
- Sorumlu: Şevval Bulut
- Durum: Tamamlandı
- Yapılan:
- ---------------------------------
| Akıllı Sporcu Performans Takip Uygulaması |
---------------------------------
|  MERHABA SPORCU!              |
|  Bugünkü Hedef: %75 Tamamlandı|
|  [|||||||||||||||------]      |
---------------------------------
| [ KALP RİTMİ ] | [ KALORİ    ] |
|    72 BPM      |   450 kcal    |
---------------------------------
| [ ADIM SAYISI] | [ AKTİF SÜRE] |
|     8.420      |    45 Dak.    |
---------------------------------
|       HAFTALIK GRAFİK (📈)      |
|  P  S  Ç  P  C  C  P          |
|  _  _  _  _  _  _  _          |
---------------------------------
|      [ ANTRENMANI BAŞLAT ]     |
---------------------------------
| [EV]  [ANALİZ]  [CİHAZ] [AYAR] |
---------------------------------

1. Ana Ekran (Gösterge Paneli)
Kullanıcının maç özetini ve maçların izlendiği merkezdir.

Üst Çubuk: Profil simgesi (Sol), Bildirimler (Sağ).

Hoş Geldin Kartı: "Merhaba [İsim], bugün performansa hazır mısın?"

Özet Widget'ları (2x2 Izgara):

Kalp Atış Hızı: [BPM]

Yakılan Kalori: [kcal]

Adım Sayısı: [Sayı]

Aktif Süre: [Dakika]

Grafik Alanı: Haftalık performans trendini gösteren basit bir çizgi grafik.

Hızlı Başlat Düğmesi: Ekranın alt ortasında, belirgin bir "Antrenmanı Başlat" (Çal simgesi) düğmesi.

2. Antrenman Takip Ekranı (Aktif Mod)
Sensörlerden gelen veriler canlı olarak aktif olan ekrandır.

Zamanlayıcı: Ekranın en üstünde, büyük puntolu kronometre.

Ana Metrikler:

Hız/Tempo (Büyük yazı tipi)

Mesafe (Orta yazı tipi)

Sensör Durumu: Sağ üst köşede küçük bir "Bağlı" ikonu (Giyilebilir sensörlü yazmaku için).

Kontrol Butonları (Alt Kısım):

[Durdur] - Turuncu/Sarı

[Bitir] - Kırmızı (Uzun basma)

3. Performans Analiz Ekranı (İstatistikler)
Geçmişe ait verilerin incelendiği bölümdür.

Takvim Görünümü: En üstte Aşırı kaydırılabilir haftalık/aylık takvim.

Detaylı Liste:

[Tarih] - [Antrenman Tipi] - [Skor/Süre]

Karşılaştırma Kartı: "Geçen haftaya göre %10 daha hızlısın" gibi bir içgörü kutucuğu.

Paylaş Butonu: Verileri aktarmak veya GitHub/Sosyal Medya üzerinden paylaşmak için sağ üstte bir simge.

4. Alt Navigasyon Menüsü (Sekme Çubuğu)
Uygulamanın her yerinden erişilebilen 4 ana sekme:

Ev (Dashboard): Genel özet.

Analiz: Detaylı veriler ve geçmiş veriler.

Cihazlar: Giyilebilir sensör ayarları düğmesi.

Profil: Kişisel hedefler ve genel ayarlar.

### Veritabanı Yapısının Oluşturulması
- Sorumlu: Nur Beyda Genç 
- Durum: Devam Ediyor
- Yapılan:
