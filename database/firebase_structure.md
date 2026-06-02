## Firebase Yapısı

### Neden hibrit mimari? (Realm + Firebase)
**Yerel (Realm/SQLite)** yüksek yazma frekansı için kullanılır.
Sensörler saniyede onlarca veri üretir, bunları doğrudan buluta yazmak
performans sorunu yaratır. Çevrimdışı çalışma da bu katmanla sağlanır.

**Firebase** uzun vadeli depolama ve gerçek zamanlı senkronizasyon için kullanılır.
Antrenör-sporcu uzaktan izleme ve anlık bildirimler bu katmandan gelir.

### Firestore Koleksiyon Yapısı
users/{userId}/workouts/{workoutId}
users/{userId}/metrics/{metricId}

### Güvenlik Kuralları
Kullanıcı yalnızca kendi dökümanlarını okuyabilir/yazabilir.
