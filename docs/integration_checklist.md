# Entegrasyon Kontrol Listesi

Son kontroller — Hafta 6

## 1. Sensör → Uygulama Veri Akışı

- [x] BLE bağlantısı kurulabiliyor
- [x] Heart Rate verisi doğru çözümleniyor (8-bit ve 16-bit format)
- [x] Bağlantı koptuğunda UI güncelleniyor
- [x] Sensör verileri yerel veritabanına yazılıyor

## 2. API → Yerel Veri Uyumu

- [x] GET /api/workoutData → Room'daki format uyuşuyor
- [x] POST /api/workoutData → JSON yapısı doğru
- [x] POST /api/sensorData → Timestamp formatı tutarlı (ISO 8601)
- [x] Hata durumlarında fallback davranış test edildi

## 3. Hata Senaryoları

| Senaryo | Beklenen Davranış | Durum |
|---------|-------------------|-------|
| BLE bağlantısı koptu | Buffer'a yaz, bağlantı gelince sync et | Test edildi |
| İnternet yok | Offline veri yerel DB'de sakla | Test edildi |
| API 500 hatası | Kullanıcıya Türkçe hata mesajı | Test edildi |
| Geçersiz JSON | Decode hatası loglanır, uygulama çökmez | Test edildi |
| Negatif profil verisi | Validasyon katmanı reddeder | Test edildi |

## 4. Platform Uyumu

- [x] iOS 16+ üzerinde test edildi
- [x] Android 8.0+ üzerinde test edildi
- [x] Dark Mode görünümü her iki platformda kontrol edildi

## 5. Veri Tutarlılığı

- [x] Kalp atışı verisi: sensör BPM → API JSON → Room DB → UI
- [x] Adım sayısı: aynı akış kontrol edildi
- [x] Kalori hesabı: algoritma çıktısı ile DB değeri eşleşiyor

## 6. Bilinen Açık Sorunlar

| ID | Açıklama | Öncelik |
|----|----------|---------|
| BUG-001 | BLE kopma anındaki veri boşluğu | Yüksek (P1) |
| BUG-002 | Profil ekranında negatif değer girişi | Orta (P2) |
| BUG-003 | Dark mode grafik eksen etiket okunurluğu | Düşük (P3) |
