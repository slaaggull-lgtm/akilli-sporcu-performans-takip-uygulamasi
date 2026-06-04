# Akıllı Sporcu Performans Takip Uygulaması - Test Stratejisi

Bu döküman, platformun mobil istemciler (iOS/Android) ve arka plan analitik motoru katmanlarında veri doğruluğunu, donanım senkronizasyonunu ve sistem kararlılığını garanti altına almak için uygulanan test metodolojilerini tanımlar.

## Test Kapsamı ve Seviyeleri

Projenin geliştirme sürecinde üç aşamalı bir test piramidi izlenmiştir:

1. Birim Testleri (Unit Tests): Analitik motorunun matematiksel algoritmalarını izole ortamda doğrulamak için yazılmıştır. Sporculardan gelen ham verilerin doğru işlendiğinden emin olunur.
2. Entegrasyon Testleri (Integration Tests): Mobil istemcilerin yerel veritabanı (SQLite) ile Firebase Firestore arasındaki asenkron veri senkronizasyon mekanizmasını denetler.
3. Donanım ve Sinyal Testleri (Hardware & BLE Verification): Bluetooth Low Energy (BLE) bağlantısının kopma senkronizasyonunu ve sensörlerden (İvmeölçer/Jiroskop) gelen veri paketlerinin (MTU) kayıpsız iletimini doğrular.

## Analitik Motoru Test Senaryoları (Python & PyTest)

Projenin `tests/test_running_analytics.py` otomasyonu kapsamında şu kritik uç senaryolar (edge-cases) test edilmektedir:
- Sıfıra Bölünme Hatası (Zero-Division): Sporcu antrenmanı başlattığı an (0. saniyede) hız ve kadans algoritmalarının çökmeden sıfır değerini döndürmesi.
- Aşırı Değer Kontrolü (Boundary Testing): Sensör hatası sebebiyle anlık nabız değerinin 250 BPM veya ivme değerinin 10G üzerine çıkması durumunda sistemin bu veriyi "gürültü" (noise) olarak algılayıp filtrelemesi.

## Mobil İstemci ve Arayüz Doğrulamaları

- iOS (XCTest) ve Android (JUnit) katmanlarında, veri analizi sırasında arayüzün donmasını engellemek için kurulan asenkron arka plan iş parçacıkları (Background Threads) performans testlerine tabi tutulmuştur.
- Cihazın internet bağlantısı kesildiğinde (Offline Mode), verilerin yerel hafızaya hatasız yazıldığı ve bağlantı geri geldiğinde Firebase'e mükerrer kayıt (double-write) oluşturmadan senkronize edildiği doğrulanmıştır.
