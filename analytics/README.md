# Analytics Modülü — Akıllı Sporcu Performans Takip

Sensörlerden gelen ham veriyi anlamlı performans metriklerine ve
antrenman önerilerine dönüştüren makine öğrenimi altyapısı.

## Scriptler

| Dosya | Açıklama |
|-------|----------|
| `running_analytics.py` | Koşu metrikleri: hız, pace, kadans, VO2Max, HR zonu |
| `export_tflite.py` | Keras modelini TFLite formatına dönüştürür |
| `optimization.py` | 3 optimizasyon stratejisi |

## Optimizasyon Stratejileri

### Strateji 1 — ACWR Kural Motoru
ACWR (Acute:Chronic Workload Ratio) hesaplayarak antrenman yükünü ayarlar.
- ACWR > 1.5 → Yük %40 azaltılır (yaralanma riski yüksek)
- ACWR 0.8–1.3 → Güvenli bölge, değişiklik yok
- ACWR < 0.8 → Yük %15 artırılabilir

### Strateji 2 — Evrimsel Algoritma
Haftalık programı "gen dizisi" olarak temsil eder ve popülasyon tabanlı
arama ile en iyi programı keşfeder. Kural motorunun ulaşamadığı
kombinasyonları bulabilir.

### Strateji 3 — XGBoost ML Modeli
Sporcu profili (yaş, HRV, uyku kalitesi, ACWR) özelliklerinden
optimal haftalık yükü tahmin eder. Yeterli veri biriktiğinde
en yüksek kişiselleştirmeyi sağlar.

## Çalıştırma

```bash
pip install -r requirements.txt

# Koşu analizi testi
python running_analytics.py

# TFLite model oluşturma
python export_tflite.py

# Optimizasyon stratejileri karşılaştırması
python optimization.py
```

## Çıktılar

- `models/running_model.tflite` → Android/iOS uygulamasına gömülür
- Konsol çıktısı → Anlık metrik ve öneri değerleri

## Kullanılan Teknolojiler

- TensorFlow / TensorFlow Lite
- scikit-learn
- XGBoost
- NumPy, Pandas
