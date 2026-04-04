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

### Kullanıcı Arayüzü (UI) ve Kullanıcı Deneyimi (UX) Tasarımı Araştırması
- Sorumlu: Asım Gökalp
- Durum: Tamamlandı
- Yapılan:

Akıllı Sporcu Performans Takip Uygulaması için kullanıcı dostu, sade ve etkileşimli bir arayüz yapısı oluşturulabilmesi amacıyla spor ve sağlık odaklı mobil uygulamalardaki güncel UI/UX trendleri araştırılmıştır. Araştırma sürecinde hem kullanıcı beklentileri hem de rakip uygulamaların tasarım yaklaşımları dikkate alınmıştır.

1. Spor Uygulamalarındaki Güncel UI/UX Trendlerinin İncelenmesi
Sporcu performans takibi yapan uygulamalarda öne çıkan tasarım yaklaşımları analiz edilmiştir. Bu kapsamda özellikle aşağıdaki noktalar değerlendirilmiştir:
Gerçek zamanlı veri gösterimi
Basit ve okunabilir gösterge panelleri
Grafik destekli performans izleme
Hedef odaklı kart yapıları
Kullanıcıyı motive eden bildirim ve geri bildirim mekanizmaları
Minimal ve dikkat dağıtmayan renk kullanımı
Araştırma sonucunda, sporcu odaklı uygulamalarda verinin karmaşık şekilde değil, sade ve anlamlı ekran bileşenleriyle sunulmasının kullanıcı deneyimini önemli ölçüde artırdığı belirlenmiştir.

2. Rakip Uygulama Analizi
Benzer alanda hizmet veren spor ve sağlık uygulamalarının arayüz yapıları incelenmiştir. Özellikle performans takibi, aktivite analizi ve hedef yönetimi sunan uygulamalardaki güçlü ve zayıf yönler değerlendirilmiştir. Bu incelemeler sonucunda:
Başarılı uygulamaların kullanıcıyı fazla menü içinde kaybetmediği
Ana ekranda en kritik verileri doğrudan sunduğu
Kullanıcının günlük, haftalık ve aylık gelişimini görselleştirdiği
Sensör bağlantısı ve veri senkronizasyonunu kolay anlaşılır şekilde yönettiği
tespit edilmiştir.
Geliştirilmesi gereken yönler arasında ise bazı uygulamalarda ekran yoğunluğunun fazla olması, veri görselleştirmesinin karmaşıklaşması ve yeni kullanıcılar için ilk kullanım deneyiminin yeterince yönlendirilmemesi yer almaktadır.

3. Kullanıcı İhtiyaçlarının Belirlenmesi
Uygulamanın hedef kitlesi olan sporcuların temel beklentileri analiz edilmiştir. Bu kapsamda kullanıcıların uygulamadan şu ihtiyaçları karşılaması beklenmektedir:
Günlük performans verilerini hızlı şekilde görebilmek
Kalp atışı, kalori, adım ve süre gibi temel metrikleri tek ekranda izleyebilmek
Kişiselleştirilmiş antrenman önerileri alabilmek
Geçmiş performansını grafiklerle takip edebilmek
Sensör bağlantı durumunu kolayca anlayabilmek
Karmaşık olmayan, hızlı öğrenilebilen bir uygulama deneyimi yaşamak
Bu değerlendirmelere göre uygulamanın özellikle sadelik, erişilebilirlik ve veri okunabilirliği üzerine kurulması gerektiği sonucuna ulaşılmıştır.

4. Wireframe ve Prototip Taslaklarının Planlanması
Araştırma sonucunda uygulama için temel ekran yapıları belirlenmiştir. Bunlar:
Ana Ekran (Dashboard): Günlük hedef, özet performans verileri ve hızlı başlat butonu
Antrenman Takip Ekranı: Canlı sensör verileri, süre, tempo ve durum bilgisi
Analiz Ekranı: Geçmiş veriler, grafikler ve karşılaştırmalı performans analizi
Cihazlar Ekranı: Giyilebilir cihaz bağlantısı ve senkronizasyon ayarları
Profil Ekranı: Kullanıcı bilgileri, hedefler ve kişisel ayarlar
Bu ekranlar için düşük sadakatli wireframe mantığında bir yapı planlanmış, ekranlar arası geçiş akışı sade ve anlaşılır olacak şekilde düşünülmüştür.

5. Kullanıcı Test Senaryolarının Oluşturulması
Uygulamanın kullanılabilirliğini değerlendirmek amacıyla temel kullanıcı test senaryoları oluşturulmuştur. Örnek senaryolar şunlardır:
Kullanıcının uygulamaya giriş yapıp ana performans ekranını görüntülemesi
Akıllı saat veya fitness cihazını uygulamaya bağlaması
Günlük antrenman başlatma ve takip ekranını kullanması
Geçmiş performans grafiklerini incelemesi
Kendisi için önerilen antrenman planını görüntülemesi
Bu senaryolar sayesinde arayüzde olası kullanım sorunlarının erken aşamada fark edilmesi hedeflenmiştir.

Genel Sonuç
Bu çalışma kapsamında, Akıllı Sporcu Performans Takip Uygulaması için modern, kullanıcı dostu ve sporcu ihtiyaçlarına uygun bir UI/UX yapısının nasıl tasarlanması gerektiği araştırılmıştır. Elde edilen bulgular doğrultusunda, uygulamanın sade bir ana ekran, güçlü veri görselleştirme yapısı, kolay cihaz entegrasyonu ve kullanıcıyı yönlendiren etkileşimli bir deneyim sunması gerektiği belirlenmiştir.


### Mobil Uygulama (iOS ve Android) Mimari Tasarımı:
- Sorumlu: Baver Katar
- Durum: Devam Ediyor
- Yapılan:


### Kişiselleştirilmiş Antrenman Planı Oluşturucu Tasarımı:
- Sorumlu: Sıla Ağgül
- Durum: Tamamlandı
- Yapılan:

Projenin temelini oluşturan kişiselleştirilmiş antrenman modülü, statik programların aksine kullanıcının biyometrik verilerini ve geçmiş spor deneyimini merkeze alan bir algoritma üzerine kurgulanmıştır. Bu aşamada; yaş, cinsiyet, boy/kilo endeksi (BMI) ve mevcut bazal metabolizma hızı gibi temel parametreler, antrenman yoğunluğunun belirlenmesinde birincil filtre olarak kullanılmıştır. Kullanıcının "sedanter", "orta seviye" veya "aktif sporcu" şeklindeki geçmiş beyanı, sakatlık riskini minimize etmek adına başlangıç ağırlıklarını ve set aralıklarını belirleyen kritik bir veri seti olarak modele dahil edilmiştir.

Tasarlanan sistemde, antrenman planlarının sadece başlangıçta değil, süreç içerisinde de evrilmesi hedeflenmiştir. Bu bağlamda, "Algılanan Zorluk Derecesi" (RPE - Rate of Perceived Exertion) skalası entegre edilerek, sporcunun her set sonundaki geri bildirimi üzerinden bir sonraki haftanın yükleme parametreleri (Volume/Intensity) otomatik olarak ayarlanmaktadır. Eğer bir kullanıcı belirli bir harekette hedef tekrar sayısına "çok kolay" ulaşıyorsa, sistem bir sonraki döngüde %5 ile %10 arasında bir ağırlık artırımı veya dinlenme süresinde daralma planlayarak gelişimi maksimize etmektedir.

Antrenman planlarının içeriği; ısınma, ana evre ve soğuma olmak üzere üç temel fazdan oluşan modüler bir kütüphane üzerinden tanımlanmıştır. Ana evre içerisinde bileşik hareketler ve izole egzersizler, sporcunun hedefine göre farklı hacimlerde dağıtılmaktadır. Her egzersiz için belirlenen set, tekrar ve tempo süreleri, kas grubunun toparlanma süreci gözetilerek takvime yerleştirilmiştir. Bu modüler yapı, kullanıcının o günkü enerji seviyesine göre antrenman süresini kısaltıp uzatabilmesine olanak tanıyan esnek bir mimariye sahiptir.

Sistemin en güçlü yanını oluşturan dinamik güncelleme mekanizması, sporcunun performans grafiklerini sürekli analiz eden bir yapı üzerine kuruludur. Kullanıcının nabız verileri veya bitirilen setlerdeki istikrarı, programın dinlenme haftası periyotlarını otomatik olarak hesaplamasını sağlar. Bu sayede sporcu aşırı antrenman riskinden korunurken, plato dönemlerini aşmak için sistem tarafından periyodik olarak farklı antrenman varyasyonları önerilerek planın güncelliği korunmaktadır. Kullanıcı verileri biriktikçe, algoritma kişiye özel "en verimli saatleri" de tahminleme yeteneğine sahip olacaktır.

Görsel tasarım aşamasında, kullanıcı deneyimini (UX) ön planda tutan bir "dashboard" yapısı kurgulanmıştır. Sporcu, o gün yapması gereken egzersizleri sadece isim olarak değil, hedef kas gruplarını gösteren anatomik haritalar eşliğinde görebilecektir. Antrenman esnasında setler arası kronometre takibi ve bir önceki antrenmanda kaldırılan ağırlığın referans olarak gösterilmesi, motivasyonu artırıcı bir unsur olarak tasarıma eklenmiştir. Bu etkileşimli yapı, sporcunun uygulamayı sadece bir liste olarak değil, bir dijital koç olarak görmesini sağlayacaktır.

Son olarak, sistemin uzun vadeli hedefleri arasında yapay zeka destekli form analizi entegrasyonu bulunmaktadır. Tasarlanan veri modeli, gelecekte kameradan alınacak görüntülerin işlenmesine uygun şekilde "iskelet sistemi koordinat verilerini" kabul edebilecek esnekliktedir. Mevcut antrenman planlayıcı, kullanıcının sadece ne yapacağını değil, neden yapması gerektiğini de açıklayan kısa bilgilendirme notları ile desteklenmiştir. Bu sayede sporcu bilinci artırılarak sürdürülebilir bir fitness alışkanlığı hedeflenmektedir.


### Performans Analiz Algoritmaları Araştırması ve Seçimi:
- Sorumlu: Şevval Bulut
- Durum: Devam Ediyor
- Yapılan:


### Veri Toplama ve Senkronizasyon Modülü Gereksinim Analizi:
- Sorumlu: Nur Beyda Genç
- Durum: Devam Ediyor
- Yapılan: 





## Hafta 3

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

Ana Ekran (Dashboard)

```
+------------------------------+
|  MERHABA SPORCU              |
|  Hedef: %75  ████████░░      |
+------------------------------+
|  Kalp: 72 BPM   | Kalori: 450|
|  Adım: 8420     | Süre: 45 dk|
+------------------------------+
|  Haftalık Grafik             |
|  P S Ç P C C P              |
|  ▂ ▃ ▅ ▄ ▆ ▇ ▅              |
+------------------------------+
|   [ ANTRENMANI BAŞLAT ]      |
+------------------------------+
|  EV | ANALİZ | CİHAZ | PROFİL|
+------------------------------+
```

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
- Durum: Tamamlandı
- Yapılan:

Veritabanı Mimarisi, Veri Modelleme ve Depolama Stratejisi Tasarımı

Genel Veritabanı Yaklaşımı: Akıllı Sporcu Performans Takip Uygulaması'nın ihtiyaç duyduğu yüksek frekanslı sensör verilerini ve uzun vadeli performans analizlerini yönetmek amacıyla hibrit bir veritabanı mimarisi tasarlanmıştır. Bu yapı, giyilebilir cihazlardan gelen anlık verilerin (nabız, adım, oksijen seviyesi) kayıpsız depolanmasını, TensorFlow Lite modelleri için veri beslemesini ve kullanıcıya geçmişe dönük raporlama sunulmasını garanti altına alır. Veritabanı tasarımında veri tutarlılığı, sorgu hızı ve ölçeklenebilirlik temel prensip olarak benimsenmiştir.

Veri Gruplandırma ve Tablo Yapıları: Sistemin işlevsel gereksinimlerini karşılamak üzere veriler mantıksal tablolar altında normalize edilerek yapılandırılmıştır:

Kullanıcı ve Profil Yönetimi (Users Table): Sporcuların fiziksel parametreleri (boy, kilo, yaş) ve fitness seviyeleri bu tabloda tutulur. Bu veriler, kişiselleştirilmiş antrenman algoritmalarının temel girdilerini oluşturur.

Ham Sensör Kayıtları (Sensor_Logs Table): Bluetooth LE üzerinden gelen anlık biyometrik veriler (BPM, SpO2, adım) zaman damgalı (timestamp) olarak bu tabloda depolanır. Yüksek veri trafiğini yönetmek adına bu tablo indekslenerek optimize edilmiştir.

Antrenman ve Performans Özeti (Workouts & Analytics Tables): Tamamlanan oturumların özet verileri ve yapay zeka modelinden dönen yorgunluk/sakatlık riski analizleri bu tablolarda ilişkilendirilerek saklanır.

Veri Senkronizasyonu ve Entegrasyonu: Mobil uygulama ile bulut sunucu arasındaki veri akışını yönetmek için gelişmiş bir senkronizasyon stratejisi kurgulanmıştır:

Firebase ve Yerel Depolama (Realm/SQLite): Sporcuların antrenman esnasında internet bağlantısı kopsa dahi veri kaybı yaşamaması için "Offline-First" yaklaşımı benimsenmiştir. Veriler önce yerel veritabanına (Realm/SQLite) yazılır, bağlantı sağlandığında Firebase ile asenkron olarak senkronize edilir.

Veri Bütünlüğü: İlişkisel modelleme (ER Diyagramı) sayesinde kullanıcılar, antrenmanlar ve analiz sonuçları arasındaki bağlar (1:N ve 1:1 ilişkiler) korunarak veri yetkilendirmesi ve güvenliği en üst seviyeye çıkarılmıştır.

Yapay Zeka (TensorFlow Lite) Veri Katmanı: Performans analiz algoritmalarının ihtiyaç duyduğu veri setlerini hızlıca çekebilmek için özel "View"lar ve sorgu optimizasyonları yapılmıştır. Modelin gelişimini izlemek amacıyla geçmiş performans verileri, makine öğrenmesi süreçlerini destekleyecek formatta (JSON/Dizi yapısı) yapılandırılmıştır.

Güvenlik ve KVKK Uyumluluğu: Veritabanı seviyesinde veri güvenliği önceliklendirilmiştir. Hassas sağlık verileri ve kişisel bilgiler şifrelenmiş kolonlarda saklanacak şekilde planlanmıştır. Erişim kontrolleri (Role-Based Access Control) ile yalnızca yetkili kullanıcıların kendi sağlık verilerine erişimi teknik olarak kısıtlanmıştır.

Gelecek Planlaması ve Genişletilebilirlik: Tasarlanan veritabanı şeması modüler bir yapıdadır. İlerleyen aşamalarda yeni sensör türleri (örneğin; uyku takip verileri veya beslenme tabloları) eklendiğinde mevcut mimariyi bozmadan kolayca entegre edilebilecek esnekliktedir. NoSQL ve Relational yapıların avantajları birleştirilerek sistemin binlerce eş zamanlı kullanıcıya hizmet verebilecek kapasiteye ulaşması hedeflenmiştir.



## Hafta 4

### SQLite Veritabanı Entegrasyonu ve Veri Modeli Oluşturma (Android):
- Sorumlu: Sıla Ağgül
- Durum: Devam Ediyor
- Yapılan:

Android platformunda veri yönetimi için endüstri standardı olan SQLite altyapısı tercih edilmiş; ancak verimliliği artırmak ve hata payını düşürmek adına "Room Persistence Library" katmanı projeye dahil edilmiştir. Room kullanımı, SQL sorgularının derleme zamanında kontrol edilmesine olanak tanıyan bir soyutlama katmanı sunarak uygulamanın çalışma anındaki olası çökmelerini engellemektedir. Bu mimari tercih, veri tabanı şemasının daha güvenli yönetilmesini ve veri erişim nesneleri sayesinde işlemlerin modüler bir hale getirilmesini sağlamıştır.

Uygulamanın omurgasını oluşturan veri modelleri; kullanıcı profili, antrenman planları, egzersiz kayıtları ve performans istatistikleri olmak üzere dört ana tablo üzerine kurgulanmıştır. Kullanıcı profili tablosunda biyometrik veriler saklanırken, antrenman planları ile egzersiz içerikleri arasında "Bire-Çok" ilişkisi kurulmuştur. Bu ilişkisel model, kullanıcının geçmişteki her bir antrenman seansını, yapılan setleri ve kaldırılan ağırlıkları en ince ayrıntısına kadar sorgulayabilmemize ve performans grafiklerini geçmişe dönük olarak oluşturabilmemize imkan tanımaktadır.

Veritabanı işlemlerinin ana iş parçacığını bloke ederek kullanıcı arayüzünde takılmalara yol açmaması için tüm operasyonlar asenkron bir yapıda tasarlanmıştır. Bu noktada Kotlin'in Coroutines yapısı ve IO kapsamı kullanılarak veritabanı sorguları arka planda yürütülmektedir. Ayrıca, büyük veri setlerinde sorgu hızını artırmak amacıyla sık kullanılan sütunlara indeksleme uygulanarak arama süreleri minimize edilmiştir. Veri tabanı erişim hızı, uygulamanın genel akıcılığını doğrudan etkileyen bir parametre olarak optimize edilmiştir.

Sistem tasarımı sadece veri depolamayı değil, verinin doğruluğunu ve gelecekteki güncellemeleri de kapsamaktadır. Kullanıcıdan gelen veriler veritabanına kaydedilmeden önce bir doğrulama katmanından geçirilerek hatalı veri girişi engellenmektedir. Ayrıca, uygulamanın ilerleyen versiyonlarında şemada yapılacak değişiklikler için versiyon yükseltme stratejisi belirlenmiş, böylece kullanıcıların mevcut antrenman verileri kaybolmadan sistemin güncellenmesi garanti altına alınmıştır. Bu süreç, veri bütünlüğünü (Data Integrity) korumak adına birincil öncelik olarak ele alınmıştır.

Veri tabanı mimarisinde "Repository" deseni uygulanarak, verinin kaynağı ile arayüz arasındaki bağ zayıflatılmış (Decoupling) ve test edilebilir bir yapı oluşturulmuştur. Bu sayede gelecekte verilerin bir kısmının bulut sistemine (Cloud Storage) taşınması durumunda arayüz kodlarında büyük değişiklikler yapılmasına gerek kalmayacaktır. Local-first yaklaşımı ile tasarlanan bu yapı, kullanıcının internet bağlantısı olmadığı durumlarda bile tüm antrenman geçmişine erişebilmesini ve yeni kayıtlar ekleyebilmesini mümkün kılmaktadır.

Son aşamada, veritabanı şeması içerisine "JSON Type Converter" yapıları eklenerek karmaşık liste verilerinin de SQLite içinde verimli bir şekilde saklanması sağlanmıştır. Örneğin, bir setin içindeki farklı dinlenme süreleri veya özel notlar, tek bir sütunda JSON formatında tutularak tablo karmaşıklığı azaltılmıştır. Bu modern veri saklama teknikleri, uygulamanın hem hafif kalmasını hem de gelecekteki karmaşık özelliklere (giyilebilir teknoloji senkronizasyonu vb.) hızlıca adapte olmasını sağlayacak bir zemin oluşturmaktadır.

![Ekran Resmi 2026-04-04 20 06 04](https://github.com/user-attachments/assets/caeb6ef4-7b99-4127-a38f-73ce026d9fae)



### Temel Performans Analizi Algoritması Geliştirme (Koşu):
- Sorumlu: Baver Katar
- Durum: Devam Ediyor
- Yapılan:


 ### REST API Entegrasyonu için Temel Veri Alma Fonksiyonları (iOS)
 - Sorumlu: Asım Gökalp
 - Durum:
 - Yapılan:

 
 ### Firebase ile Temel Kullanıcı Kimlik Doğrulama Entegrasyonu (Android):
 - Sorumlu: Şevval Bulut
 - Durum: Devam Ediyor
 - Yapılan:


 ### Bluetooth LE Veri Senkronizasyon Entegrasyonu (iOS):
 - Sorumlu: Nur Beyda Genç
 - Durum: Devam Ediyor
 - Yapılan:

   
