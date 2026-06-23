# 📌 Proje Durumu

Bu bölüm, projenin **şu an çalışan** kısımları ile **planlanan (yol haritası)** kısımlarını net olarak ayırır. Aşağıdaki mimari ve teknoloji başlıkları projenin hedef tasarımını anlatır; mevcut sürümde çalışan kapsam burada işaretlenmiştir.

## ✅ Çalışan Sürüm (Demo)

Canlı: https://akilli-sporcu-takip.onrender.com

Web tabanlı sakatlanma risk analiz arayüzü — uçtan uca çalışır:

- 5 metrikle veri girişi: ortalama nabız, maksimum nabız, süre, ivme varyansı, yorgunluk
- Kural tabanlı risk motoru ile anlık risk skoru (0–100) ve üç bantlı sınıflandırma (Düşük / Orta / Yüksek)
- Rastgele sensör verisi simülasyonu
- Antrenman geçmişi tablosu ve özet istatistikler
- CSV formatında rapor dışa aktarımı

Kaynak kodu: [`web/index.html`](web/index.html)

## 🚧 Geliştirme Aşamasında (Faz 2)

Aşağıdaki bileşenlerin mimari tasarımı ve kod iskeleti hazırdır; tam entegrasyon devam etmektedir:

| Bileşen | Durum |
| ------- | ----- |
| Native Android (Java / MVVM) istemci | İskelet hazır, entegrasyon sürüyor |
| Native iOS (Swift) istemci | İskelet hazır, entegrasyon sürüyor |
| Flask REST API backend | Temel uç noktalar mevcut, risk motoruna bağlanıyor |
| BLE sensör entegrasyonu | Donanım gereksinimi — simülasyon ile temsil ediliyor |
| Firebase senkronizasyon + FCM bildirim | Planlandı |
| TensorFlow Lite tabanlı ML modeli | Kural tabanlı motordan ML modeline geçiş planlandı |

> Not: Bu sürümdeki risk skoru, açıklanabilir **kural tabanlı** bir motorla üretilir. ML tabanlı modele geçiş Faz 2 kapsamındadır.
