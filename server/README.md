# Backend API — Akıllı Sporcu Performans Takip

Flask tabanlı REST API. Mobil uygulamadan gelen antrenman ve sensör verilerini yönetir.

## Kurulum (isteğe bağlı, yerel test için)

```bash
pip install -r requirements.txt
python app.py


API http://localhost:5000 adresinde çalışır.

Endpointler
Method	URL	Açıklama
GET	/	Sağlık kontrolü
POST	/auth/register	Kullanıcı kaydı
POST	/auth/login	Giriş
POST	/auth/logout	Çıkış
GET	/api/workoutData	Antrenmanları listele
POST	/api/workoutData	Antrenman ekle
POST	/api/sensorData	Sensör verisi gönder
GET	/api/sensorData	Sensör verilerini listele
GET	/api/performance/summary	Performans özeti
Örnek İstek (register)
POST /auth/register



JSON
{
  "email": "sporcu@example.com",
  "password": "sifre123",
  "name": "Ayşe Kaya"
}




Mimari
app.py → Uygulama giriş noktası
routes/auth.py → Kimlik doğrulama (kayıt, giriş, çıkış)
routes/workout.py → Antrenman ve sensör veri yönetimi
Güvenlik Notları
Mevcut hâliyle mock JWT token kullanılmaktadır. Üretim ortamı için Firebase Authentication veya gerçek JWT kütüphanesi entegre edilmelidir.
