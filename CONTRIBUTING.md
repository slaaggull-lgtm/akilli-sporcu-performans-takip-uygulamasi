#  Akıllı Sporcu Performans Takip Uygulaması - Katkı Sağlama Rehberi

Bu döküman, projemizin 13 farklı branch ve 196 commit'e ulaşan geliştirme sürecinde, ekip üyelerimizin (**Sıla, Nur Beyda, Şevval, Baver, Asım**) kod kalitesini korumak ve Git iş akışını (workflow) yönetmek için uyguladığı katı standartları içermektedir.

##  Branch (Dal) Adlandırma Standartları

Projede karmaşayı önlemek amacıyla yeni açılan her branch belirli bir kurala göre isimlendirilmiş ve ana omurgaya (`main`) o şekilde entegre edilmiştir:

- `feature/` : Sisteme eklenen yeni özellikler (Örn: `feature/ble-connection`, `feature/mediapipe-pose`)
- `bugfix/` : Çözülen teknik hatalar (Örn: `bugfix/main-thread-block`, `bugfix/floating-point-error`)
- `docs/` : Dokümantasyon ve rapor güncellemeleri (Örn: `docs/system-overview`)

##  Commit Mesajı Formatı

Proje geçmişinin (Commit History) izlenebilir olması için her ekip üyesi commit mesajlarını şu standart kurumsal formatta atmıştır:

-  **feat:** Yeni bir özellik eklendiğinde (`feat: Core Bluetooth notification modu aktif edildi`)
-  **fix:** Bir hata düzeltildiğinde (`fix: roundToNearestPlates metodu ile yuvarlama sapması giderildi`)
-  **docs:** Sadece dokümantasyon değişikliği yapıldığında (`docs: Mimari ve kurulum dökümanları eklendi`)
-  **style:** Kodun çalışmasını etkilemeyen görsel/stil düzenlemelerinde

## Pull Request (PR) ve Code Review Süreci

1. Hiçbir ekip üyesi doğrudan `main` branch'ine doğrudan kontrolsüz kod basamaz.
2. Yazılan kod ilgili `feature/` veya `bugfix/` branch'inden `main` branch'ine bir **Pull Request (PR)** açılarak talep edilir.
3. PR açıldıktan sonra en az 1 ekip üyesi kodu satır satır inceleyip (Code Review) onay vermeden kod `main` ile birleştirilemez (Merge).
