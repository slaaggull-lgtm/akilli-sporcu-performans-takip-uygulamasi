# Akıllı Sporcu Performans Takip Uygulaması - Güvenlik Politikası

Bu döküman, platform üzerinde işlenen sporcu biyometrik verilerinin, sensör telemetrilerinin ve kullanıcı hesaplarının güvenliğini sağlamak amacıyla uygulanan teknik mimariyi ve veri koruma standartlarını tanımlar.

## Yasal Uyum ve Veri İzolasyonu (KVKK & GDPR)

Uygulama, nitelikli kişisel veri statüsünde olan sağlık ve performans verilerini işlediği için katı kurallara tabidir:
- KVKK ve GDPR Madde 9 kapsamında, sporcuların nabız (BPM), hareket kısıtları ve vücut analiz verileri veri tabanında maskelenerek saklanır.
- Çoklu kiracılık (Multi-tenancy) mimarisinde veri sızıntılarını önlemek amacıyla, Firebase üzerinde her sporcunun sadece kendi ID'sine ait dökümanları okuyup yazabilmesini sağlayan kurallar (Security Rules) aktif edilmiştir.

## Veri İletimi ve Depolama Güvenliği

- **Taşıma Esnasındaki Veri (Data in Transit):** Mobil istemciler ile sunucu/bulut katmanı arasındaki tüm veri trafiği TLS 1.3 protokolü üzerinden şifrelenir. Güvenlik duvarını aşmaya yönelik sahte sertifika saldırılarına karşı SSL Pinning tekniği uygulanmıştır.
- **Durağan Veri (Data at Rest):** Cihazların yerel hafızasında (çevrimdışı modda) tutulan sensör logları ve antrenman kayıtları AES-256-GCM simetrik şifreleme algoritması kullanılarak SQL/Realm katmanında kilitlenir.

## Kimlik Doğrulama ve API Güvenliği

- Kullanıcı giriş işlemleri ve oturum yönetimleri asenkron JSON Web Token (JWT) mimarisi ile korunmaktadır.
- Sunucu katmanına yapılan tüm API istekleri, her 24 saatte bir yenilenen Bearer Token kontrolünden geçmek zorundadır. Yetkisiz veya imzasız gelen paketler gateway seviyesinde doğrudan reddedilir.
