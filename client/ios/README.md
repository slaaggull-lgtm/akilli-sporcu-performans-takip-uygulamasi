# iOS Modülü — Akıllı Sporcu Performans Takip

Native iOS uygulaması. SwiftUI ve Core Bluetooth ile geliştirilmiştir.

## Gereksinimler

- iOS 16+
- Swift 5.9+
- Xcode 15+

## Kullanılan Teknolojiler

| Teknoloji | Amaç |
|-----------|------|
| Core Bluetooth | BLE sensör bağlantısı (Apple Watch, Garmin vb.) |
| URLSession + Codable | REST API iletişimi ve JSON çözümleme |
| NSCache | Görsel önbellekleme |
| Mach kernel API | CPU ve bellek kullanımı ölçümü |
| SwiftUI | Kullanıcı arayüzü |
| Combine / async-await | Asenkron veri akışı |

## Klasör Yapısı

## Bluetooth Veri Akışı

1. `CBCentralManager` Bluetooth durumunu izler
2. Heart Rate servisi UUID'si (0x180D) taranır
3. Cihaz bulununca bağlantı kurulur
4. `Notify` isteğiyle veri akışı başlar
5. Her nabız güncellemesinde `@Published heartRateBPM` güncellenir

## API Bağlantısı

```swift
WorkoutAPIService.shared.fetchWorkoutPlans { result in
    switch result {
    case .success(let plans): print(plans)
    case .failure(let error): print(error.localizedDescription)
    }
}
```

## Performans Optimizasyonları (Hafta 5 bulguları)

| Metrik | Önceki | Sonraki | İyileşme |
|--------|--------|---------|----------|
| Bellek | 185 MB | 97 MB | %47 azalma |
| CPU | %78 | %24 | %69 azalma |
| FPS | 38 | 60 | Akıcı |
| Açılış süresi | 2.8 sn | 1.1 sn | %61 azalma |
