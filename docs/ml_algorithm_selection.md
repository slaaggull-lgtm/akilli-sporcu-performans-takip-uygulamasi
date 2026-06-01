# Makine Öğrenimi Algoritma Seçim Raporu

## İncelenen Algoritmalar

| Algoritma | Açıklama | Kullanım Amacı |
|-----------|----------|----------------|
| Linear Regression | Doğrusal ilişki modeli | Sürekli değer tahmini |
| Decision Tree | Ağaç tabanlı sınıflandırma | Hızlı karar destek |
| Random Forest | Çoklu karar ağacı (ensemble) | Yüksek doğruluklu sınıflandırma |
| SVM | Hiper düzlem sınıflandırıcı | Yüksek doğruluk gerektiren durumlar |
| KNN | En yakın komşu | Benzerlik tabanlı analiz |
| Neural Network (TFLite) | Derin öğrenme | Karmaşık örüntü analizi |

## Karşılaştırmalı Analiz

| Algoritma | Avantaj | Dezavantaj | Uygunluk |
|-----------|---------|------------|----------|
| Decision Tree | Yorumlanabilir, hızlı | Aşırı öğrenme riski | Yüksek |
| Random Forest | Stabil, yüksek doğruluk | Hesaplama maliyeti | Orta |
| SVM | Güçlü genelleme | Büyük veriyle yavaş | Orta |
| KNN | Basit | Yüksek hesaplama maliyeti | Düşük |
| Neural Network | Karmaşık ilişkileri öğrenir | Veri/eğitim maliyeti yüksek | Çok Yüksek |

## Seçilen Modeller

**1. Decision Tree** — Düşük hesaplama maliyeti ve yorumlanabilirliği sayesinde
mobil uygulamada hızlı karar mekanizması sağlar.

**2. TensorFlow Lite tabanlı Neural Network** — Doğrusal olmayan ilişkileri
öğrenebilme yeteneği ve mobil optimizasyon desteğiyle yüksek doğruluk sunar.

## Seçim Kriterleri

- Mobil cihazlarda çalışabilirlik
- Düşük gecikme süresi (< 100ms)
- Orta ölçekli veriyle yüksek performans
- Yorumlanabilirlik (sporcu/antrenöre açıklanabilmeli)

## Model Eğitim Süreci

1. Veri temizleme (eksik değer, aykırı değer tespiti)
2. Normalizasyon (MinMaxScaler — 0-1 aralığı)
3. %80 eğitim / %20 test ayrımı
4. Hiperparametre optimizasyonu (Grid Search + Cross-validation)
5. TFLite dönüşümü ve model küçültme (quantization)

## Performans Değerlendirme Metrikleri

- **Accuracy**: Genel doğruluk
- **Precision**: Hassasiyet
- **Recall**: Duyarlılık
- **F1-Score**: Dengesiz veri durumlarında birleşik metrik
- **MAE**: Sürekli tahminlerde ortalama mutlak hata
