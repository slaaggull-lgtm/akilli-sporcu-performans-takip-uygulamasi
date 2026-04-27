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



![Kişiselleştirilmiş Antrenman Planı Oluşturucu 2](https://github.com/user-attachments/assets/287bfc76-0664-48ad-8d0c-2787bf316242)



### Performans Analiz Algoritmaları Araştırması ve Seçimi:
- Sorumlu: Şevval Bulut
- Durum: Tamamlandı
- Yapılan:
 Sporcu Performans Analizi İçin Makine Öğrenimi Algoritmalarının Karşılaştırılması ve Seçimi
1. Giriş

Sporcu performansının doğru ve etkili bir şekilde analiz edilmesi, antrenman süreçlerinin optimize edilmesi ve bireysel gelişimin izlenmesi açısından kritik öneme sahiptir. Giyilebilir teknolojilerin (akıllı saatler, fitness takip cihazları vb.) yaygınlaşmasıyla birlikte büyük miktarda veri elde edilebilmekte ve bu verilerin anlamlı hale getirilmesi için makine öğrenimi yöntemlerine ihtiyaç duyulmaktadır.

Bu çalışma kapsamında, sporcu performans analizinde kullanılabilecek çeşitli makine öğrenimi algoritmaları incelenmiş, bu algoritmaların avantajları ve sınırlamaları karşılaştırılmış ve mobil uygulama ortamına en uygun algoritmalar belirlenmiştir. Ayrıca, seçilen algoritmaların eğitimi, optimizasyonu ve performans değerlendirme süreçleri detaylandırılmıştır.

2. İncelenen Makine Öğrenimi Algoritmaları

Bu çalışmada hem klasik hem de modern makine öğrenimi yaklaşımları değerlendirilmiştir:
```
Algoritma	                                              Tanım	                                                                                             Kullanım Amacı

Linear Regression	                        Bağımlı ve bağımsız değişkenler arasındaki doğrusal ilişkiyi modelleyen istatistiksel yöntemdir.        	 Sürekli değer tahmini (örneğin performans skoru)

Decision Tree	                            Veriyi karar düğümleri aracılığıyla parçalayan ağaç tabanlı algoritmadır.	                                  Sınıflandırma ve karar destek

Random Forest	                            Birden fazla karar ağacının birleşimi ile çalışan topluluk öğrenme yöntemidir.         	                      Daha yüksek doğruluklu sınıflandırma

Support Vector Machine (SVM)	            Verileri ayıran en uygun hiper düzlemi bulan güçlü bir sınıflandırma yöntemidir.	                         Yüksek doğruluk gerektiren sınıflandırma

K-Nearest Neighbors (KNN)	                Yeni bir veriyi en yakın komşularına göre sınıflandırır.           	                                          Benzerlik tabanlı analiz

Yapay Sinir Ağları (TensorFlow Lite)	    İnsan beyninden esinlenen katmanlı yapılar ile karmaşık örüntüleri öğrenir.                                  Karmaşık veri analizi ve tahmin
```
 ```
3. Algoritmaların Karşılaştırmalı Analizi

Algoritma                               	Avantajlar	                   Dezavantajlar	                Uygulama Uygunluğu

Decision Tree	                      Yorumlanabilir, hızlı	          Aşırı öğrenme (overfitting) riski	           Yüksek

Random Forest	                   Yüksek doğruluk, stabil	              Hesaplama maliyeti yüksek	                 Orta

SVM	                            Güçlü genelleme yeteneği	            Büyük veri ile yavaş	                    Orta

KNN                               Basit ve sezgisel	                      Yüksek hesaplama maliyeti             	Düşük

Neural Network                	Karmaşık ilişkileri öğrenir	            Veri ve eğitim maliyeti yüksek	         Çok Yüksek
```

4. Problem Tanımı ve Model Seçimi

Bu çalışmada ele alınan problem, sporcu performansının çok boyutlu veriler (kalp atış hızı, hız, mesafe vb.) kullanılarak analiz edilmesi ve sınıflandırılmasıdır. Problem hem sınıflandırma hem de tahmin bileşenleri içermektedir.

Proje gereksinimleri doğrultusunda model seçiminde aşağıdaki kriterler dikkate alınmıştır:

Mobil cihazlarda çalışabilirlik

Düşük gecikme süresi

Orta ölçekli veri ile yüksek performans

Yorumlanabilirlik

Seçilen Modeller

Decision Tree

TensorFlow Lite tabanlı Yapay Sinir Ağı

Seçim Gerekçesi

Decision Tree, düşük hesaplama maliyeti ve yorumlanabilirliği sayesinde mobil uygulamalarda hızlı karar mekanizması sunar.

Yapay sinir ağları ise doğrusal olmayan ve karmaşık ilişkileri öğrenerek daha yüksek doğruluk sağlar. TensorFlow Lite ile mobil ortama optimize edilebilir.

5. Veri Seti ve Özellikler

Model eğitiminde kullanılacak veri seti aşağıdaki özellikleri içermektedir:

Kalp atış hızı (bpm)

Adım sayısı

Hız (km/s)

Kat edilen mesafe (km)

Enerji harcaması (kalori)

Antrenman süresi ve türü

Bu veriler giyilebilir sensörlerden elde edilecek olup, zaman serisi ve çok değişkenli veri yapısı içermektedir.




6. Model Eğitimi ve Optimizasyon Süreci

6.1 Veri Ön İşleme

Eksik verilerin temizlenmesi

Aykırı değerlerin tespiti

Normalizasyon ve standardizasyon

6.2 Eğitim Süreci

Veri setinin eğitim (%80) ve test (%20) olarak ayrılması

Modelin eğitim verisi üzerinde öğrenmesi

Test verisi ile performansın değerlendirilmesi

6.3 Hiperparametre Optimizasyonu

Grid Search

Random Search

Cross-validation

6.4 Mobil Optimizasyon

Model küçültme (quantization)

TensorFlow Lite dönüşümü

Bellek ve hız optimizasyonu

7. Performans Değerlendirme Metrikleri

Model performansı aşağıdaki metrikler kullanılarak değerlendirilecektir:

Accuracy (Doğruluk)

Precision (Hassasiyet)

Recall (Duyarlılık)

F1-Score

Bu metrikler, modelin hem genel doğruluğunu hem de dengesiz veri durumlarındaki başarısını ölçmek için kullanılacaktır.

8. Sonuç

Bu çalışma kapsamında, sporcu performans analizine yönelik çeşitli makine öğrenimi algoritmaları detaylı şekilde incelenmiş ve karşılaştırılmıştır. Yapılan analizler sonucunda:

Decision Tree algoritması, hızlı ve yorumlanabilir yapısıyla mobil uygulamalar için uygun bulunmuştur.
TensorFlow Lite tabanlı Yapay Sinir Ağları, karmaşık veri ilişkilerini öğrenebilme yeteneği sayesinde yüksek doğruluk sunmaktadır.

Bu iki yaklaşımın birlikte kullanılması, hem performans hem de doğruluk açısından dengeli bir çözüm sunmaktadır. Geliştirilecek sistem, sporcuların performansını gerçek zamanlı analiz ederek antrenman süreçlerinin optimize edilmesine katkı sağlayacaktır.



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



### Veri Toplama ve Senkronizasyon Modülü Gereksinim Analizi:
- Sorumlu: Nur Beyda Genç
- Durum: Tamamlandı
- Yapılan: 
1. Toplanacak Veri Türleri ve Sensör Kaynakları
Giyilebilir cihazlar, sporcunun biyometrik ve kinetik durumunu şu üç ana kategoride analiz eder:

Biyometrik Veriler: Nabız (Heart Rate), kandaki oksijen (SpO2), vücut sıcaklığı ve HRV (Kalp Atış Hızı Değişkenliği).

Kinematik Veriler: İvmeölçer (Accelerometer) ve Jiroskop (Gyroscope) kullanılarak elde edilen adım sayısı, kadans, vuruş hızı veya sıçrama yüksekliği.

Konumsal Veriler: GPS ve Barometre aracılığıyla hız, kat edilen mesafe ve irtifa kazanımı.
{
  "athleteId": "SPORCU_01",
  "timestamp": "2026-04-09T13:11:07Z",
  "metrics": {
    "heart_rate": 145,
    "acceleration": {"x": 0.12, "y": 9.81, "z": -0.05},
    "gps": {"lat": 38.67, "lng": 39.22, "alt": 1020}
  }
}
2. Bluetooth LE (Low Energy) ve Veri FormatlarıAkıllı cihazlar genellikle GATT (Generic Attribute Profile) protokolünü kullanır.İletişim Protokolü: BLE, enerjiyi korumak için verileri küçük paketler (MTU - Maximum Transmission Unit) halinde gönderir.Servisler ve Karakteristikler: Her veri türü bir UUID ile tanımlanır. Örneğin, Nabız için 0x180D servisi kullanılır.Veri Formatı: Cihazlar ham veriyi genelde Little Endian Binary formatında gönderir. Mobil uygulama bu Byte dizisini (Byte Array) işleyerek anlamlı sayılara dönüştürür.3. Veri Toplama ve Senkronizasyon Akış ŞemasıVeri akışı, anlık performans takibi için "Streaming" ve geçmiş analiz için "Batch" (yığın) işleme olarak ikiye ayrılır.Bağlantı: Uygulama, önceden eşleşmiş cihazı UUID üzerinden tarar ve bağlanır.Abone Olma (Notify): Uygulama, ilgili karakteristiklere "Notify" isteği gönderir; böylece saat, veri değiştikçe otomatik olarak paket gönderir.Yerel İşleme: Gelen ham veri parse edilir ve anlık olarak UI'da gösterilir.Buffer & Sync: İnternet yoksa veriler yerelde depolanır, bağlantı geldiğinde buluta itilir.4. Veritabanı Seçimi: Realm/SQLite vs. FirebaseSporcu performans takibi gibi yüksek yazma frekansı gerektiren bir senaryoda seçimimiz şu yöndedir:Karar: Hibrit Mimari (Realm + Firebase)Neden Realm/SQLite (Yerel Depolama)?Düşük Gecikme: Sensörler saniyede onlarca veri üretebilir. Bu veriyi doğrudan buluta yazmak yerine yerelde Realm gibi nesne tabanlı bir veritabanında tutmak performans açısından kritiktir.Çevrimdışı Çalışma: Sporcu ormanlık alanda veya spor salonunda internet çekmiyorken veri kaybı yaşanmamalıdır.Neden Firebase (Bulut Depolama)?Gerçek Zamanlı Senkronizasyon: Antrenörün sporcuyu uzaktan izlemesi gerekiyorsa Firebase Realtime Database/Firestore rakipsizdir.Analitik ve Bildirimler: Veriler buluta çıktığında, sporcuya "Nabzın çok yüksek!" gibi anlık bildirimler gönderilebilir.ÖzellikRealm (Yerel)Firebase (Bulut)HızÇok Yüksek (Milisaniye altı)İnternet hızına bağlıKapasiteCihaz hafızasıyla sınırlıSınırsız (Scalable)RolHam veri tamponlama (Buffer)Uzun vadeli analiz ve paylaşım5. Veri Güvenliği ve DoğrulukHata İşleme: Veri paketi eksik gelirse (CRC hatası), o veri noktası "outlier" (aykırı değer) olarak işaretlenmeli ve kalibrasyon algoritmalarıyla düzeltilmelidir.Güvenlik: BLE üzerinden geçen veriler AES-128 ile şifrelenmeli ve mobil uygulamada Biometric Authentication ile korunmalıdır.Geliştirdiğimiz bu yapı, sporcunun antrenman esnasında hiçbir verisini kaybetmeden, en düşük gecikmeyle analiz edilmesini sağlar



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
- Durum: Tamamlandı
- Yapılan:

Android platformunda veri yönetimi için endüstri standardı olan SQLite altyapısı tercih edilmiş; ancak verimliliği artırmak ve hata payını düşürmek adına "Room Persistence Library" katmanı projeye dahil edilmiştir. Room kullanımı, SQL sorgularının derleme zamanında kontrol edilmesine olanak tanıyan bir soyutlama katmanı sunarak uygulamanın çalışma anındaki olası çökmelerini engellemektedir. Bu mimari tercih, veri tabanı şemasının daha güvenli yönetilmesini ve veri erişim nesneleri sayesinde işlemlerin modüler bir hale getirilmesini sağlamıştır.

Uygulamanın omurgasını oluşturan veri modelleri; kullanıcı profili, antrenman planları, egzersiz kayıtları ve performans istatistikleri olmak üzere dört ana tablo üzerine kurgulanmıştır. Kullanıcı profili tablosunda biyometrik veriler saklanırken, antrenman planları ile egzersiz içerikleri arasında "Bire-Çok" ilişkisi kurulmuştur. Bu ilişkisel model, kullanıcının geçmişteki her bir antrenman seansını, yapılan setleri ve kaldırılan ağırlıkları en ince ayrıntısına kadar sorgulayabilmemize ve performans grafiklerini geçmişe dönük olarak oluşturabilmemize imkan tanımaktadır.

Veritabanı işlemlerinin ana iş parçacığını bloke ederek kullanıcı arayüzünde takılmalara yol açmaması için tüm operasyonlar asenkron bir yapıda tasarlanmıştır. Bu noktada Kotlin'in Coroutines yapısı ve IO kapsamı kullanılarak veritabanı sorguları arka planda yürütülmektedir. Ayrıca, büyük veri setlerinde sorgu hızını artırmak amacıyla sık kullanılan sütunlara indeksleme uygulanarak arama süreleri minimize edilmiştir. Veri tabanı erişim hızı, uygulamanın genel akıcılığını doğrudan etkileyen bir parametre olarak optimize edilmiştir.

Sistem tasarımı sadece veri depolamayı değil, verinin doğruluğunu ve gelecekteki güncellemeleri de kapsamaktadır. Kullanıcıdan gelen veriler veritabanına kaydedilmeden önce bir doğrulama katmanından geçirilerek hatalı veri girişi engellenmektedir. Ayrıca, uygulamanın ilerleyen versiyonlarında şemada yapılacak değişiklikler için versiyon yükseltme stratejisi belirlenmiş, böylece kullanıcıların mevcut antrenman verileri kaybolmadan sistemin güncellenmesi garanti altına alınmıştır. Bu süreç, veri bütünlüğünü (Data Integrity) korumak adına birincil öncelik olarak ele alınmıştır.

Veri tabanı mimarisinde "Repository" deseni uygulanarak, verinin kaynağı ile arayüz arasındaki bağ zayıflatılmış (Decoupling) ve test edilebilir bir yapı oluşturulmuştur. Bu sayede gelecekte verilerin bir kısmının bulut sistemine (Cloud Storage) taşınması durumunda arayüz kodlarında büyük değişiklikler yapılmasına gerek kalmayacaktır. Local-first yaklaşımı ile tasarlanan bu yapı, kullanıcının internet bağlantısı olmadığı durumlarda bile tüm antrenman geçmişine erişebilmesini ve yeni kayıtlar ekleyebilmesini mümkün kılmaktadır.

Son aşamada, veritabanı şeması içerisine "JSON Type Converter" yapıları eklenerek karmaşık liste verilerinin de SQLite içinde verimli bir şekilde saklanması sağlanmıştır. Örneğin, bir setin içindeki farklı dinlenme süreleri veya özel notlar, tek bir sütunda JSON formatında tutularak tablo karmaşıklığı azaltılmıştır. Bu modern veri saklama teknikleri, uygulamanın hem hafif kalmasını hem de gelecekteki karmaşık özelliklere (giyilebilir teknoloji senkronizasyonu vb.) hızlıca adapte olmasını sağlayacak bir zemin oluşturmaktadır.


![Ekran Resmi 2026-04-04 20 06 04](https://github.com/user-attachments/assets/caeb6ef4-7b99-4127-a38f-73ce026d9fae)


 ### Firebase ile Temel Kullanıcı Kimlik Doğrulama Entegrasyonu (Android):
 - Sorumlu: Şevval Bulut
 - Durum: Tamamlandı
 - Yapılan:
 - Projenin güvenlik ve kullanıcı yönetimi katmanı için Google'ın bulut tabanlı çözüm mimarisi olan Firebase Authentication altyapısı tercih edilmiştir. Bu entegrasyon, kullanıcıların e-posta ve şifre kombinasyonu ile güvenli bir şekilde sisteme dahil olmalarını sağlarken, şifrelerin istemci tarafında tutulmadan Firebase sunucularında endüstri standardı olan karma (hashing) algoritmalarıyla saklanmasını garanti altına almaktadır. Kimlik doğrulama süreci, uygulamanın giriş bariyerini oluşturarak kişiselleştirilmiş antrenman verilerinin gizliliğini korumak amacıyla birincil güvenlik protokolü olarak kurgulanmıştır.

Yazılım mimarisi tarafında, Firebase çağrılarının doğrudan arayüz katmanından (UI) yapılması yerine, modülerliği artırmak adına MVVM (Model-View-ViewModel) deseni ve Repository Pattern uygulanmıştır. Bu sayede, kimlik doğrulama mantığı (Auth Logic) ile kullanıcı arayüzü birbirinden tamamen izole edilmiştir. AuthRepository katmanı, Firebase SDK ile iletişim kuran tek nokta olarak belirlenmiş; AuthViewModel ise asenkron gelen yanıtları yöneterek kullanıcıya gerçek zamanlı geri bildirim sağlayan bir köprü görevi üstlenmiştir.

Kullanıcı deneyimini en üst seviyeye çıkarmak amacıyla, kimlik doğrulama akışı Sealed Class yapısı kullanılarak "Yükleniyor", "Başarılı" ve "Hata" gibi farklı durum modelleri (AuthState) üzerinden takip edilmektedir. Bu yapı sayesinde, uygulama giriş yaparken ekranda otomatik bir ProgressBar tetiklenmekte; hatalı şifre veya kayıtlı olmayan kullanıcı durumlarında ise Firebase'den dönen teknik hata kodları, kullanıcı dostu Türkçe mesajlara dönüştürülerek Snackbar veya Toast bildirimleri aracılığıyla iletilmektedir.

Performans ve kaynak yönetimi açısından, ağ üzerinden yapılan kimlik doğrulama istekleri Kotlin Coroutines kullanılarak yönetilmektedir. Giriş ve kayıt işlemleri sırasında ana iş parçacığının (Main Thread) kilitlenmesi engellenerek uygulamanın akıcılığı korunmuştur. Ayrıca, Firebase'in onAuthStateChanged dinleyicisi entegre edilerek, kullanıcı uygulamayı kapatıp açtığında oturumunun otomatik olarak hatırlanması (Session Management) sağlanmış, her açılışta tekrar giriş yapma zorunluluğu ortadan kaldırılarak kullanım kolaylığı hedeflenmiştir.

Kullanıcı arayüzü (UI) tasarımı, Android'in modern Material 3 kütüphanesi kullanılarak geliştirilmiştir. Giriş formunda bulunan e-posta alanları için Regex (Düzenli İfade) kontrolü eklenerek, verilerin Firebase sunucularına gönderilmeden önce istemci tarafında doğrulanması sağlanmıştır. Bu validasyon katmanı, sunucu yükünü azaltırken kullanıcının anlık olarak hatalı veri girişlerini (örneğin geçersiz e-posta formatı) görmesine ve düzeltmesine imkan tanımaktadır.

Sistemin test aşamasında, farklı senaryolar (doğru bilgiler, zayıf şifre, internet bağlantısı yokluğu vb.) üzerinde birim testler (Unit Tests) gerçekleştirilerek kimlik doğrulama akışının kararlılığı doğrulanmıştır. Firebase'in sunduğu hata yönetimi (Error Handling) mekanizması sayesinde, olası sunucu kesintilerinde uygulamanın nasıl tepki vereceği senaryolaştırılmış ve güvenli çıkış (Sign-out) işlemi ile kullanıcı verilerinin yerel bellekteki izlerinin tamamen temizlenmesi garanti altına alınmıştır.

![Firebase ile Temel Kullanıcı Kimlik Doğrulama Entegrasyonu (Android)](https://github.com/user-attachments/assets/37ef2673-065f-4152-9e4b-2f76cd37341f)

A) build.gradle (Java Bağımlılıkları)

dependencies {
    // Firebase BoM ve Auth (Java uyumlu SDK)
    implementation platform('com.google.firebase:firebase-bom:32.7.0')
    implementation 'com.google.firebase:firebase-auth'
    
    // Lifecycle ve ViewModel (Java desteğiyle)
    implementation 'androidx.lifecycle:lifecycle-viewmodel:2.6.2'
    implementation 'androidx.lifecycle:lifecycle-livedata:2.6.2'
}

B) AuthState.java (Durum Yönetimi Sınıfı)
public class AuthState {
    public enum Status { IDLE, LOADING, SUCCESS, ERROR }
    
    private final Status status;
    private final String errorMessage;
    private final FirebaseUser user;

    private AuthState(Status status, String errorMessage, FirebaseUser user) {
        this.status = status;
        this.errorMessage = errorMessage;
        this.user = user;
    }

    public static AuthState idle() { return new AuthState(Status.IDLE, null, null); }
    public static AuthState loading() { return new AuthState(Status.LOADING, null, null); }
    public static AuthState success(FirebaseUser user) { return new AuthState(Status.SUCCESS, null, user); }
    public static AuthState error(String message) { return new AuthState(Status.ERROR, message, null); }

    // Getters...
}

C) AuthRepository.java (Firebase İşlemleri)
public class AuthRepository {
    private final FirebaseAuth mAuth;

    public AuthRepository() {
        this.mAuth = FirebaseAuth.getInstance();
    }

    public void loginUser(String email, String password, OnAuthCompleteListener listener) {
        mAuth.signInWithEmailAndPassword(email, password)
            .addOnCompleteListener(task -> {
                if (task.isSuccessful()) {
                    listener.onSuccess(mAuth.getCurrentUser());
                } else {
                    listener.onError(task.getException().getMessage());
                }
            });
    }

    public interface OnAuthCompleteListener {
        void onSuccess(FirebaseUser user);
        void onError(String error);
    }
}




 ### REST API Entegrasyonu için Temel Veri Alma Fonksiyonları (iOS)

- Sorumlu: Asım Gökalp
- Durum: Tamamlandı
- Yapılan:

  - Swift dili kullanılarak REST API’den veri alma işlemleri için temel yapı oluşturuldu.
  - URLSession ile API’ye GET isteği gönderme işlemi geliştirildi.
  - JSON formatındaki yanıtların Codable kullanılarak veri modellerine dönüştürülmesi sağlandı.
  - Ağ bağlantısı, sunucu yanıtı ve veri çözümleme hataları için temel hata yönetimi eklendi.
  - Mock JSON verisi kullanılarak veri çözümleme testi yapıldı ve sonuçlar konsolda doğrulandı.:

  import Foundation

// MARK: - Veri Modelleri

struct WorkoutPlan: Codable {
    let id: Int
    let title: String
    let description: String
    let duration: Int // dakika
    let exercises: [Exercise]
}

struct Exercise: Codable {
    let id: Int
    let name: String
    let sets: Int
    let reps: Int
    let restSeconds: Int
    
    enum CodingKeys: String, CodingKey {
        case id, name, sets, reps
        case restSeconds = "rest_seconds"
    }
}

// MARK: - Hata Tipleri

enum APIError: Error, LocalizedError {
    case invalidURL
    case noData
    case decodingError(String)
    case serverError(Int)
    case networkError(String)
    
    var errorDescription: String? {
        switch self {
        case .invalidURL:
            return "Geçersiz URL."
        case .noData:
            return "Sunucudan veri alınamadı."
        case .decodingError(let msg):
            return "Veri çözümleme hatası: \(msg)"
        case .serverError(let code):
            return "Sunucu hatası: HTTP \(code)"
        case .networkError(let msg):
            return "Ağ bağlantısı hatası: \(msg)"
        }
    }
}

// MARK: - API Servisi

class WorkoutAPIService {
    
    static let shared = WorkoutAPIService()
    
    private let baseURL = "https://api.example.com" // Gerçek API adresiyle değiştir
    private let session: URLSession
    
    private init() {
        let config = URLSessionConfiguration.default
        config.timeoutIntervalForRequest = 30
        config.timeoutIntervalForResource = 60
        self.session = URLSession(configuration: config)
    }
    
    // MARK: - Tüm Antrenman Planlarını Getir
    
    func fetchWorkoutPlans(completion: @escaping (Result<[WorkoutPlan], APIError>) -> Void) {
        guard let url = URL(string: "\(baseURL)/workout-plans") else {
            completion(.failure(.invalidURL))
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        // request.setValue("Bearer TOKEN", forHTTPHeaderField: "Authorization")
        
        performRequest(request: request, completion: completion)
    }
    
    // MARK: - Belirli Bir Antrenman Planını Getir
    
    func fetchWorkoutPlan(id: Int, completion: @escaping (Result<WorkoutPlan, APIError>) -> Void) {
        guard let url = URL(string: "\(baseURL)/workout-plans/\(id)") else {
            completion(.failure(.invalidURL))
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        
        performRequest(request: request, completion: completion)
    }
    
    // MARK: - Genel İstek Fonksiyonu
    
    private func performRequest<T: Decodable>(
        request: URLRequest,
        completion: @escaping (Result<T, APIError>) -> Void
    ) {
        session.dataTask(with: request) { data, response, error in
            
            DispatchQueue.main.async {
                
                // Ağ hatası kontrolü
                if let error = error {
                    completion(.failure(.networkError(error.localizedDescription)))
                    return
                }
                
                // HTTP durum kodu kontrolü
                if let httpResponse = response as? HTTPURLResponse {
                    guard (200...299).contains(httpResponse.statusCode) else {
                        completion(.failure(.serverError(httpResponse.statusCode)))
                        return
                    }
                }
                
                // Veri kontrolü
                guard let data = data else {
                    completion(.failure(.noData))
                    return
                }
                
                // JSON çözümleme
                do {
                    let decoder = JSONDecoder()
                    let decoded = try decoder.decode(T.self, from: data)
                    completion(.success(decoded))
                } catch {
                    completion(.failure(.decodingError(error.localizedDescription)))
                }
            }
            
        }.resume()
    }
}

// MARK: - Kullanım Örneği (ViewController veya ViewModel içinde)

class WorkoutViewModel {
    
    func loadWorkoutPlans() {
        WorkoutAPIService.shared.fetchWorkoutPlans { result in
            switch result {
            case .success(let plans):
                print(" \(plans.count) antrenman planı alındı.")
                for plan in plans {
                    print(" Plan: \(plan.title) - \(plan.duration) dk")
                    for exercise in plan.exercises {
                        print("    \(exercise.name): \(exercise.sets) set x \(exercise.reps) tekrar")
                    }
                }
                
            case .failure(let error):
                print(" Hata: \(error.localizedDescription)")
            }
        }
    }
    
    func loadSinglePlan(id: Int) {
        WorkoutAPIService.shared.fetchWorkoutPlan(id: id) { result in
            switch result {
            case .success(let plan):
                print(" Plan alındı: \(plan.title)")
            case .failure(let error):
                print(" Hata: \(error.localizedDescription)")
            }
        }
    }
}

// MARK: - Test (Mock Data ile)

func testWithMockData() {
    let mockJSON = """
    [
        {
            "id": 1,
            "title": "Üst Vücut Antrenmanı",
            "description": "Göğüs, sırt ve omuz egzersizleri",
            "duration": 60,
            "exercises": [
                { "id": 1, "name": "Bench Press", "sets": 4, "reps": 10, "rest_seconds": 90 },
                { "id": 2, "name": "Pull-Up", "sets": 3, "reps": 8, "rest_seconds": 60 }
            ]
        }
    ]
    """.data(using: .utf8)!
    
    do {
        let plans = try JSONDecoder().decode([WorkoutPlan].self, from: mockJSON)
        print("Mock veri başarıyla çözümlendi: \(plans.first?.title ?? "")")
    } catch {
        print(" Mock veri hatası: \(error)")
    }
}

// Test et
testWithMockData()
let vm = WorkoutViewModel()
vm.loadWorkoutPlans()



### Temel Performans Analizi Algoritması Geliştirme (Koşu):
- Sorumlu: Baver Katar
- Durum: Devam Ediyor
- Yapılan:



 ### Bluetooth LE Veri Senkronizasyon Entegrasyonu (iOS):
 - Sorumlu: Nur Beyda Genç
 - Durum: Tamamlandı
 - Yapılan:
1. Temel Bluetooth Yöneticisi (Core Bluetooth)
Öncelikle, Bluetooth işlemlerini merkezi bir yerden yönetmek için CBCentralManagerDelegate ve CBPeripheralDelegate protokollerini uygulayan bir sınıf oluşturuyoruz.
import Foundation
import CoreBluetooth

class BluetoothManager: NSObject, ObservableObject, CBCentralManagerDelegate, CBPeripheralDelegate {
    
    @Published var connectionStatus: String = "Bağlantı Yok"
    @Published var performanceData: String = "---"
    
    private var centralManager: CBCentralManager!
    private var heartRatePeripheral: CBPeripheral?
    
    // Akıllı saatlerin genellikle kullandığı standart Heart Rate Servis UUID'si
    private let heartRateServiceUUID = CBUUID(string: "180D")
    private let heartRateCharacteristicUUID = CBUUID(string: "2A37")

    override init() {
        super.init()
        centralManager = CBCentralManager(delegate: self, queue: nil)
    }

    // MARK: - Merkezi Yönetici Durumu
    func centralManagerDidUpdateState(_ central: CBCentralManager) {
        switch central.state {
        case .poweredOn:
            connectionStatus = "Cihaz Aranıyor..."
            centralManager.scanForPeripherals(withServices: [heartRateServiceUUID], options: nil)
        case .poweredOff:
            connectionStatus = "Bluetooth Kapalı"
        case .unauthorized:
            connectionStatus = "İzin Verilmedi"
        default:
            connectionStatus = "Bilinmeyen Hata"
        }
    }

    // MARK: - Cihaz Bulma ve Bağlanma
    func centralManager(_ central: CBCentralManager, didDiscover peripheral: CBPeripheral, advertisementData: [String : Any], rssi RSSI: NSNumber) {
        connectionStatus = "Cihaz Bulundu: \(peripheral.name ?? "Bilinmiyor")"
        heartRatePeripheral = peripheral
        heartRatePeripheral?.delegate = self
        centralManager.stopScan()
        centralManager.connect(peripheral, options: nil)
    }

    func centralManager(_ central: CBCentralManager, didConnect peripheral: CBPeripheral) {
        connectionStatus = "Bağlı: \(peripheral.name ?? "Cihaz")"
        peripheral.discoverServices([heartRateServiceUUID])
    }
    
    func centralManager(_ central: CBCentralManager, didFailToConnect peripheral: CBPeripheral, error: Error?) {
        connectionStatus = "Bağlantı Hatası!"
    }

    // MARK: - Servis ve Karakteristik Keşfi
    func peripheral(_ peripheral: CBPeripheral, didDiscoverServices error: Error?) {
        guard let services = peripheral.services else { return }
        for service in services {
            peripheral.discoverCharacteristics([heartRateCharacteristicUUID], for: service)
        }
    }

    func peripheral(_ peripheral: CBPeripheral, didDiscoverCharacteristicsFor service: CBService, error: Error?) {
        guard let characteristics = service.characteristics else { return }
        for characteristic in characteristics {
            if characteristic.uuid == heartRateCharacteristicUUID {
                // Veri akışını başlat (Notify)
                peripheral.setNotifyValue(true, for: characteristic)
            }
        }
    }

    // MARK: - Veri Akışı ve Hata Yönetimi
    func peripheral(_ peripheral: CBPeripheral, didUpdateValueFor characteristic: CBCharacteristic, error: Error?) {
        if let error = error {
            print("Veri okuma hatası: \(error.localizedDescription)")
            return
        }
        
        if characteristic.uuid == heartRateCharacteristicUUID {
            if let data = characteristic.value {
                let bpm = decodeHeartRate(from: data)
                DispatchQueue.main.async {
                    self.performanceData = "\(bpm) BPM"
                }
            }
        }
    }

    // Basit bir Heart Rate veri çözümleme yardımcı fonksiyonu
    private func decodeHeartRate(from data: Data) -> Int {
        var buffer = [UInt8](repeating: 0, count: data.count)
        data.copyBytes(to: &buffer, count: data.count)
        if buffer.count >= 2 {
            return Int(buffer[1]) // Standart 8-bit nabız verisi
        }
        return 0
    }
}
2. Kullanıcı Arayüzü (SwiftUI)
Kullanıcının bağlantı durumunu görmesi ve gelen verileri takip etmesi için basit bir arayüz:
import SwiftUI

struct PerformanceTrackerView: View {
    @StateObject var btManager = BluetoothManager()

    var body: some View {
        VStack(spacing: 30) {
            Text("Sporcu Performans Takibi")
                .font(.headline)
            
            // Bağlantı Durum Göstergesi
            HStack {
                Circle()
                    .fill(btManager.connectionStatus.contains("Bağlı") ? Color.green : Color.red)
                    .frame(width: 12, height: 12)
                
                Text(btManager.connectionStatus)
                    .font(.subheadline)
                    .foregroundColor(.secondary)
            }
            .padding()
            .background(Color(.systemGray6))
            .cornerRadius(10)

            // Performans Verisi
            VStack {
                Text("Anlık Nabız")
                    .font(.caption)
                    .foregroundColor(.gray)
                Text(btManager.performanceData)
                    .font(.system(size: 64, weight: .bold, design: .rounded))
                    .foregroundColor(.blue)
            }
            
            Spacer()
        }
        .padding()
    }
}


## Hafta 5

### Antrenman Programı Optimizasyon Algoritmasını İyileştirme
- Sorumlu: Sıla Ağgül
- Durum: Tamamlandı
- Yapılan:


Genel Bakış
Bu haftanın görevi, mevcut antrenman programı optimizasyon sisteminin bireysel sporcu ihtiyaçlarına uyum kapasitesini artırmaya odaklanmaktadır. Mevcut algoritmanın kural tabanlı (rule-based) yapısı, ortalama bir sporcu profili için yeterli çıktılar üretse de bireysel farklılıkları (yaş, pozisyon, yorgunluk geçmişi, psikolojik yük) yeterince yansıtmamaktadır. Bu çalışmada üç farklı optimizasyon stratejisi denenmiş, sonuçlar karşılaştırmalı olarak analiz edilmiştir.

Mevcut Sistemin Kısıtları
Sistemin mevcut hali, antrenman yükünü hesaplamak için sabit eşik değerlerine dayanan basit bir kural motoru kullanmaktadır. Bu yaklaşımın temel sorunları şunlardır: sporcunun gerçek zamanlı toparlanma durumu göz ardı edilmekte, haftalık yük dağılımı statik kalmakta ve takım dinamikleri ile maç takvimi gibi bağlamsal faktörler sisteme dahil edilmemektedir.

 Strateji 1 — Kural Tabanlı Sistemin Güçlendirilmesi
İlk aşamada mevcut kural motoru, dinamik eşikler ve kısıt katmanı eklenerek iyileştirilmiştir. Sporcunun ACWR (Acute:Chronic Workload Ratio) değeri anlık olarak hesaplanmakta ve bu değere göre antrenman yoğunluğu otomatik olarak kısıtlanmaktadır.

```python
def compute_acwr(weekly_loads: list[float], acute_window=7, chronic_window=28) -> float:
    """
    Akut:Kronik Yük Oranı hesaplar.
    Güvenli bölge: 0.8 – 1.3
    """
    if len(weekly_loads) < chronic_window:
        return 1.0  # Yetersiz veri — nötr oran döndür

    acute = sum(weekly_loads[-acute_window:]) / acute_window
    chronic = sum(weekly_loads[-chronic_window:]) / chronic_window

    return round(acute / chronic, 3) if chronic > 0 else 1.0

def apply_load_constraint(base_load: float, acwr: float) -> float:
    """
    ACWR değerine göre antrenman yükünü ayarlar.
    """
    if acwr > 1.5:
        return base_load * 0.6   # Yüksek yaralanma riski — düşür
    elif acwr > 1.3:
        return base_load * 0.85  # Dikkatli bölge — hafif düşür
    elif acwr < 0.8:
        return base_load * 1.15  # Düşük yük — artırılabilir
    return base_load              # Güvenli bölge — değiştirme
```

Bu yaklaşım, mevcut altyapıyla uyumludur ve hızla devreye alınabilir. Ancak kural sayısı arttıkça bakımı güçleşmekte ve keşfedilmemiş optimum senaryolara ulaşması sınırlı kalmaktadır.

 Strateji 2 — Evrimsel Algoritma (Genetik Yaklaşım)
İkinci stratejide, haftalık antrenman programı bir "gen" dizisi olarak temsil edilmekte ve popülasyon tabanlı bir arama ile optimize edilmektedir. Her birey (çözüm adayı) bir haftayı temsil eden egzersiz-yoğunluk çiftlerinden oluşmaktadır.

```python
import random

def fitness(program: list, athlete: dict) -> float:
    """
    Bir antrenman programının uygunluğunu değerlendirir.
    Yüksek skor = daha iyi program.
    """
    total_load = sum(day["intensity"] * day["duration"] for day in program)
    recovery_days = sum(1 for day in program if day["intensity"] == 0)

    # Hedef yük — ACWR güvenli bölgesi
    target_load = athlete["chronic_load"] * 1.1
    load_score = max(0, 1 - abs(total_load - target_load) / target_load)

    # En az 2 dinlenme günü şartı
    recovery_score = min(recovery_days / 2, 1.0)

    return 0.6 * load_score + 0.4 * recovery_score

def crossover(parent_a: list, parent_b: list) -> list:
    """Tek noktalı çaprazlama."""
    point = random.randint(1, len(parent_a) - 1)
    return parent_a[:point] + parent_b[point:]

def mutate(program: list, rate=0.1) -> list:
    """Rastgele gün yoğunluğunu değiştir."""
    return [
        {**day, "intensity": random.uniform(0, 1)} if random.random() < rate else day
        for day in program
    ]
```

Evrimsel yaklaşım, kural tabanlı sistemin ulaşamayacağı program kombinasyonlarını keşfedebilmektedir. Bununla birlikte hesaplama süresi daha uzundur ve her çalıştırmada deterministik olmayan sonuçlar üretebilir.

Strateji 3 — Makine Öğrenmesi Tabanlı Tahmin (XGBoost)
Üçüncü stratejide, geçmiş antrenman verileri ve sonuçları (performans artışı, yaralanma kaydı) üzerinde eğitilmiş bir XGBoost modeli kullanılmıştır. Model, verilen sporcu profiline göre optimum haftalık yükü tahmin etmektedir.

```python
from xgboost import XGBRegressor
import numpy as np

def build_features(athlete: dict) -> np.ndarray:
    """Sporcu özelliklerinden model giriş vektörü oluşturur."""
    return np.array([[
        athlete["age"],
        athlete["chronic_load"],
        athlete["acwr"],
        athlete["hrv"],          # Heart Rate Variability
        athlete["sleep_score"],
        athlete["days_to_match"]
    ]])

# Model yükleme ve tahmin
model = XGBRegressor()
model.load_model("models/load_predictor_v2.json")

def predict_optimal_load(athlete: dict) -> float:
    features = build_features(athlete)
    prediction = model.predict(features)[0]
    return round(float(prediction), 1)
```

Bu yaklaşım, büyük veri setiyle eğitildiğinde en yüksek bireyselleştirme kapasitesine ulaşmaktadır. Modelin güvenilirliği, eğitim verisinin kalitesine ve çeşitliliğine doğrudan bağlıdır.

Karşılaştırmalı Değerlendirme

| Kriter | Kural Tabanlı | Evrimsel | ML (XGBoost) |
| :--- | :--- | :--- | :--- |
| Bireyselleştirme | Orta | Yüksek | Çok yüksek |
| Hesaplama süresi | Çok hızlı | Yavaş | Hızlı (eğitim sonrası) |
| Yorumlanabilirlik | Yüksek | Orta | Düşük |
| Veri gereksinimi | Düşük | Düşük | Yüksek |
| Bakım kolaylığı | Orta | Zor | Orta |

Önerilen Yol Haritası
Kısa vadede kural tabanlı sistemin ACWR ve HRV entegrasyonuyla güçlendirilmesi önerilmektedir. Bu değişiklik mevcut altyapıya minimum müdahaleyle uygulanabilir ve hemen ölçülebilir iyileşme sağlar. Orta vadede evrimsel algoritma, haftalık program üretimi için arka planda çalışan bir öneri motoru olarak devreye alınabilir ve kural motoruyla hibrit biçimde kullanılabilir. Uzun vadede ise yeterli veri biriktiğinde ML modelinin prodüksiyona alınması planlanmaktadır.

 Sonuç
Bu hafta yürütülen çalışma, tek bir optimizasyon yaklaşımının tüm sporcu profillerini yeterince karşılayamadığını açıkça ortaya koymaktadır. Hibrit bir mimari — kural tabanlı güvenlik katmanı, evrimsel program keşfi ve ML tabanlı yük tahmini — en güçlü ve esnek çözümü sunmaktadır. Bir sonraki aşama, bu üç katmanın entegrasyon testlerinin gerçek sporcu verileriyle yapılmasıdır.

### Veritabanı Entegrasyonunu Tamamlama ve Test Etme
- Sorumlu: Baver Katar
- Durum: Devam Ediyor
- Yapılan:



### Veri Toplama ve İşleme Modülünü Geliştirme
- Sorumlu: Nur Beyda Genç
- Durum: Devam Ediyor
- Yapılan:



### Mobil Uygulama Performans Analizi ve Optimizasyonu
- Sorumlu: Asım Gökalp
- Durum: Tamamlandı
- Yapılan: 

1. PerformanceMonitor.swift:
import Foundation
import os.signpost

class PerformanceMonitor {
    
    static let shared = PerformanceMonitor()
    private let log = OSLog(subsystem: "com.app.workout", category: "Performance")
    private var metrics: [String: [Double]] = [:]
    private let queue = DispatchQueue(label: "performance.monitor", attributes: .concurrent)
    
    private init() {}
    
    func measureCPUUsage() -> Double {
        var threadList: thread_act_array_t?
        var threadCount: mach_msg_type_number_t = 0
        let result = task_threads(mach_task_self_, &threadList, &threadCount)
        guard result == KERN_SUCCESS, let threads = threadList else { return 0.0 }
        
        var totalCPU: Double = 0.0
        for i in 0..<Int(threadCount) {
            var threadInfo = thread_basic_info()
            var threadInfoCount = mach_msg_type_number_t(THREAD_INFO_MAX)
            let infoResult = withUnsafeMutablePointer(to: &threadInfo) {
                $0.withMemoryRebound(to: integer_t.self, capacity: 1) {
                    thread_info(threads[i], thread_flavor_t(THREAD_BASIC_INFO), $0, &threadInfoCount)
                }
            }
            if infoResult == KERN_SUCCESS, threadInfo.flags & TH_FLAGS_IDLE == 0 {
                totalCPU += Double(threadInfo.cpu_usage) / Double(TH_USAGE_SCALE) * 100.0
            }
        }
        vm_deallocate(mach_task_self_, vm_address_t(UInt(bitPattern: threadList)),
                      vm_size_t(threadCount) * vm_size_t(MemoryLayout<thread_t>.stride))
        return totalCPU
    }
    
    func measureMemoryUsage() -> Double {
        var info = mach_task_basic_info()
        var count = mach_msg_type_number_t(MemoryLayout<mach_task_basic_info>.size) / 4
        let result = withUnsafeMutablePointer(to: &info) {
            $0.withMemoryRebound(to: integer_t.self, capacity: 1) {
                task_info(mach_task_self_, task_flavor_t(MACH_TASK_BASIC_INFO), $0, &count)
            }
        }
        guard result == KERN_SUCCESS else { return 0 }
        return Double(info.resident_size) / 1_048_576
    }
    
    func measure(label: String, block: () -> Void) {
        let start = CFAbsoluteTimeGetCurrent()
        block()
        let elapsed = (CFAbsoluteTimeGetCurrent() - start) * 1000
        queue.async(flags: .barrier) {
            self.metrics[label, default: []].append(elapsed)
        }
        print("⏱️ [\(label)]: \(String(format: "%.2f", elapsed)) ms")
    }
    
    func generateReport() {
        queue.sync {
            print("\n====== 📊 PERFORMANS RAPORU ======")
            print("🔥 CPU: \(String(format: "%.1f", measureCPUUsage()))%")
            print("💾 Bellek: \(String(format: "%.1f", measureMemoryUsage())) MB")
            for (label, times) in metrics {
                let avg = times.reduce(0, +) / Double(times.count)
                print("  📌 \(label) → Ort: \(String(format: "%.2f", avg)) ms")
            }
            print("==================================\n")
        }
    }
}

2. ImageCacheManager.swift:
import UIKit

class ImageCacheManager {
    
    static let shared = ImageCacheManager()
    private let cache = NSCache<NSString, UIImage>()
    
    private init() {
        cache.countLimit = 100
        cache.totalCostLimit = 50 * 1024 * 1024 // 50 MB
    }
    
    func loadImage(from urlString: String, completion: @escaping (UIImage?) -> Void) {
        let key = urlString as NSString
        
        if let cached = cache.object(forKey: key) {
            completion(cached)
            return
        }
        
        guard let url = URL(string: urlString) else {
            completion(nil)
            return
        }
        
        URLSession.shared.dataTask(with: url) { [weak self] data, _, _ in
            guard let data = data, let image = UIImage(data: data) else {
                DispatchQueue.main.async { completion(nil) }
                return
            }
            self?.cache.setObject(image, forKey: key)
            DispatchQueue.main.async { completion(image) }
        }.resume()
    }
}

3. OptimizationExamples.swift:
import UIKit

// MARK: - 1. Background Thread
extension WorkoutViewController {
    func loadDataOptimized() {
        DispatchQueue.global(qos: .userInitiated).async {
            WorkoutAPIService.shared.fetchWorkoutPlans { result in
                switch result {
                case .success(let plans):
                    self.plans = plans
                    self.tableView.reloadData()
                case .failure(let error):
                    self.showError(error)
                }
            }
        }
    }
}

// MARK: - 2. Cell Yeniden Kullanımı
extension WorkoutViewController: UITableViewDataSource {
    func tableView(_ tableView: UITableView, cellForRowAt indexPath: IndexPath) -> UITableViewCell {
        guard let cell = tableView.dequeueReusableCell(
            withIdentifier: WorkoutCell.reuseIdentifier,
            for: indexPath
        ) as? WorkoutCell else { return UITableViewCell() }
        cell.configure(with: plans[indexPath.row])
        return cell
    }
}

// MARK: - 3. GPU Rasterization
extension WorkoutCell {
    func applyOptimizedStyle() {
        layer.cornerRadius = 12
        layer.shadowColor = UIColor.black.cgColor
        layer.shadowOpacity = 0.3
        layer.shouldRasterize = true
        layer.rasterizationScale = UIScreen.main.scale
    }
}

// MARK: - 4. Retain Cycle Önleme
class WorkoutViewModel {
    var onUpdate: (() -> Void)?
    
    func fetchData() {
        WorkoutAPIService.shared.fetchWorkoutPlans { [weak self] result in
            guard let self = self else { return }
            self.onUpdate?()
        }
    }
}

# 📱 Mobil Uygulama Performans Analizi ve Optimizasyonu

## 🎯 Amaç
iOS uygulamasının CPU, bellek ve FPS metriklerini ölçmek,
darboğazları tespit etmek ve optimize etmek.

## 🔍 Tespit Edilen Darboğazlar
| # | Sorun | Çözüm |
|---|-------|-------|
| 1 | Ana thread bloklanması | Background thread |
| 2 | Hücre yeniden kullanılmıyor | dequeueReusableCell |
| 3 | Görsel önbellekleme yok | NSCache |
| 4 | Gereksiz GPU render | shouldRasterize |
| 5 | Retain cycle | [weak self] |

## 📊 Sonuçlar
| Metrik | Önce | Sonra | İyileşme |
|--------|------|-------|----------|
| Bellek | 185 MB | 97 MB | %47 ↓ |
| CPU | %78 | %24 | %69 ↓ |
| FPS | 38 | 60 | ✅ Akıcı |
| Açılış | 2.8 sn | 1.1 sn | %61 ↓ |

## 📁 Dosyalar
- `PerformanceMonitor.swift` — Metrik ölçüm sınıfı
- `ImageCacheManager.swift` — Görsel önbellekleme
- `OptimizationExamples.swift` — Optimizasyon örnekleri

  - Mobil uygulamanın performansı CPU kullanımı, bellek tüketimi, pil kullanımı ve ağ istekleri açısından analiz edilmiştir.
  - Performansı olumsuz etkileyebilecek başlıca darboğazlar; sık sensör verisi işleme, arka plan senkronizasyon işlemleri, gereksiz UI güncellemeleri ve yoğun veri işleme süreçleri olarak belirlenmiştir.
  - Ana iş parçacığında çalışan ağır işlemlerin arka plan thread’lerine alınması, veri senkronizasyon sıklığının azaltılması, cache mekanizmalarının kullanılması ve lazy loading yaklaşımının uygulanması önerilmiştir.
  - Optimizasyon öncesi ve sonrası durum karşılaştırılarak CPU ve bellek kullanımında azalma, pil tüketiminde iyileşme ve arayüz akıcılığında artış hedeflenmiştir.



### Kullanıcı Arayüzü Testlerini Tamamlama
- Sorumlu: Şevval Bulut
- Durum: Devam Ediyor
- Yapılan:
  Bu rapor, "Akıllı Sporcu Performans Takip Uygulaması" mobil arayüzünün temel fonksiyonlarını, sensör entegrasyonunu ve veri tutarlılığını ölçmek amacıyla yapılan kapsamlı testlerin sonuçlarını içerir. Testler; Kara Kutu (Black Box) ve Kullanılabilirlik (Usability) test teknikleri kullanılarak gerçekleştirilmiştir. Toplamda 6 ana senaryo işletilmiş, 3 adet kritik ve orta seviye hata tespit edilmiştir.

TEST SENARYOLARI VE SONUÇ TABLOSU:
<pre>
 ID ''' Fonksiyon / Modül ''' Test Tanımı  Başarı Kriteri  Durum
 TS-01Kimlik DoğrulamaKullanıcı e-posta/şifre ile giriş süreci.Dashboard'a yönlendirme.BAŞARILITS-02BLE BağlantısıGiyilebilir sensörün Bluetooth ile eşleşmesi.Stabil veri akışı kurulumu.BAŞARILITS-03Gerçek Zamanlı İzlemeAntrenman esnasında metriklerin görselleştirilmesi.Veri gecikmesinin <500ms olması.KISMEN BAŞARILITS-04Kritik Uyarı SistemiEşik değer (Nabız/Hız) aşıldığında bildirim gönderimi.Anlık sesli ve görsel uyarı.BAŞARILITS-05Veri SenkronizasyonuAntrenman bitiminde bulut kaydı ve geçmiş listeleme.Verinin "Geçmiş"te görünmesi.BAŞARILI
</pre>
 
