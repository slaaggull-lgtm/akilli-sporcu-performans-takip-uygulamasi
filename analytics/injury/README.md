# 🛡️ Sakatlık Önleme Modülü (Injury Prevention Module)

Bu modül, sporcu biyometrik ve kinematik verilerini analiz ederek
sakatlık riskini gerçek zamanlı olarak hesaplar ve kişiselleştirilmiş
öneriler üretir.

## 📁 Dosya Yapısı
analytics/injury/
├── InjuryRiskAnalyzer.py   # Ana analiz motoru
├── InjuryRiskTests.py      # Birim testler (9 senaryo)
└── README.md

## 🔬 Kullanılan Metrikler

| Metrik | Kaynak | Ağırlık |
|--------|--------|---------|
| ACWR (Akut:Kronik Yük Oranı) | Haftalık yük geçmişi | %40 |
| HRV Düşüş Oranı (RMSSD) | Giyilebilir sensör | %30 |
| Dinlenik Nabız Trendi | Akıllı saat | %15 |
| Yerle Temas Süresi (GCT) | İvmeölçer | %15 |

## ⚙️ Kurulum ve Çalıştırma

```bash
pip install numpy
python InjuryRiskAnalyzer.py   # Örnek sporcu analizi
python InjuryRiskTests.py      # Tüm birim testleri çalıştır
```

## 🔗 Entegrasyon

`InjuryRiskAnalyzer`, `analytics/running_analytics.py` modülünden
gelen `RunningAnalytics` metrik çıktılarıyla doğrudan beslenir.
TFLite modeli, `risk_score` değerini gerçek zamanlı mobil geri
bildirim için kullanır.

## 📚 Akademik Referanslar

- Gabbett, T.J. (2016). *The training-injury prevention paradox.*
  British Journal of Sports Medicine, 50(5), 273-280.
- Plews, D.J. et al. (2013). *HRV and training load monitoring.*
  International Journal of Sports Physiology & Performance.
