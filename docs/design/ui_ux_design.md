# UI/UX Tasarım Sistemi — Akıllı Sporcu Performans Takip

## Tasarım Felsefesi

Premium Karanlık Mod (Dark Mode) temelli tasarım.
Sporcu odaklı: veri okunurluğu ve motivasyon ön planda.

## Renk Paleti

| Renk | Hex Kodu | Kullanım Amacı |
|------|----------|----------------|
| Neon Teal | `#00F0FF` | Ana vurgular, CTA butonları |
| Electric Blue | `#007AFF` | Bilgi kartları, ikincil eylemler |
| Glowing Green | `#39FF14` | Yüksek performans, başarı göstergeleri |
| Neon Purple | `#BD00FF` | Yüksek yoğunluklu bölge gösterimi |
| Dark Background | `#0A0A0F` | Ana arkaplan |
| Card Surface | `#141420` | Kart arkaplanları |

## Tipografi

| Kullanım | Yazı Tipi | Ağırlık |
|----------|-----------|---------|
| Başlıklar, metrik gösterimi | Outfit | 700 (Bold) |
| Gövde metni, etiketler | Inter | 400 (Regular) |

## Glassmorphism Efekti

Kart bileşenlerinde derinlik hissi için:
```css
backdrop-filter: blur(20px);
background: rgba(255, 255, 255, 0.05);
border: 1px solid rgba(255, 255, 255, 0.1);
border-radius: 16px;
```

## Temel Ekranlar

### 1. Ana Ekran (Dashboard)
- Kullanıcı aktivite özeti
- Anlık nabız (kalp ritim grafiğiyle)
- Yakılan aktif kalori
- Egzersiz süresi
- Cam kart bileşenleri

### 2. Performans Analiz Ekranı (Analytics)
- Büyük dairesel neon gösterge (VO2 Max skoru)
- Haftalık toparlanma durumu
- Kalp atışı trend grafiği

### 3. Antrenman Planları Ekranı (Workout Plans)
- Kaydırılabilir haftalık takvim
- AI motor önerilen günlük program
- Hızlı antrenman başlatma

### 4. Profil Ekranı (User Profile)
- Fiziksel parametreler grid görünümü
- Apple HealthKit / Google Fit entegrasyon ayarları

## Geri Bildirim Döngüsü

1. **RPE Değerlendirmesi** — Antrenman sonrası 1-10 Borg skalası
2. **CSAT Anketi** — Profil sekmesinde tek tıkla memnuniyet puanı

## Platform Uyumu

| Platform | Tasarım Sistemi |
|----------|----------------|
| Android | Material Design 3 (MD3) |
| iOS | Human Interface Guidelines (HIG) |
