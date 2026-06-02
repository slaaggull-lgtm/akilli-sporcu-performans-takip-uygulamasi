# Android Modülü — Akıllı Sporcu Performans Takip

Native Android uygulaması. Clean Architecture + MVVM deseniyle geliştirilmiştir.

## Gereksinimler

- Android 8.0+ (API 26)
- Java 11
- Firebase projesi (google-services.json)

## Kullanılan Teknolojiler

| Teknoloji | Amaç |
|-----------|------|
| Room Persistence Library | SQLite ORM — yerel veri depolama |
| Firebase Authentication | Kullanıcı kimlik doğrulama |
| Firebase Firestore | Bulut veritabanı senkronizasyonu |
| TensorFlow Lite | Cihaz üzerinde performans analizi |
| MVVM + LiveData | Mimari desen |

## Klasör Yapısı

```
data/
  local/
    AppDatabase.java      → Room veritabanı (Singleton)
    WorkoutDao.java       → SQL sorgu arayüzü
    entity/
      User.java           → Kullanıcı varlığı
      Workout.java        → Antrenman varlığı
  remote/
    AuthRepository.java   → Firebase Auth işlemleri
domain/
  WorkoutPlanGenerator.java → Antrenman planı algoritması
presentation/
  AuthState.java          → Kimlik doğrulama durum modeli
```

## Mimari

**Clean Architecture** katmanları:
- **Presentation** → ViewModel + AuthState
- **Domain** → WorkoutPlanGenerator (iş mantığı)
- **Data** → Room (yerel) + Firebase (uzak)

**Offline-First** yaklaşımı: Veriler önce Room'a yazılır,
internet bağlantısı sağlandığında Firebase ile senkronize edilir.

## Güvenlik

- Firebase Authentication (e-posta/şifre)
- AES-256 veri şifreleme (planlanan)
- JWT token yönetimi
