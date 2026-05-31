import UIKit

/// Gorsel once bellekleme yoneticisi.
/// NSCache kullanarak indirilen gorselleri bellekte tutar,
/// ayni URL icin tekrar ag istegi yapilmasini onler.
class ImageCacheManager {

    static let shared = ImageCacheManager()

    /// NSCache otomatik bellek temizleme yapar (dusuk bellek uyarisinda)
    private let cache = NSCache<NSString, UIImage>()

    private init() {
        cache.countLimit = 100          // Maksimum 100 gorsel
        cache.totalCostLimit = 50 * 1024 * 1024  // Maksimum 50 MB
    }

    // MARK: - Gorsel Yukleme

    /// URL'den gorsel yukler. Once onbellege bakar, yoksa indirir.
    /// - Parameters:
    ///   - urlString: Gorsel URL'si
    ///   - completion: Sonuc (UIImage veya nil)
    func loadImage(from urlString: String, completion: @escaping (UIImage?) -> Void) {
        let key = urlString as NSString

        // Once bellege bak
        if let cached = cache.object(forKey: key) {
            completion(cached)
            return
        }

        guard let url = URL(string: urlString) else {
            completion(nil)
            return
        }

        // Bellekte yoksa indir
        URLSession.shared.dataTask(with: url) { [weak self] data, _, _ in
            guard let data = data, let image = UIImage(data: data) else {
                DispatchQueue.main.async { completion(nil) }
                return
            }

            // Bellege kaydet ve ana thread'de dondur
            self?.cache.setObject(image, forKey: key)
            DispatchQueue.main.async { completion(image) }
        }.resume()
    }

    // MARK: - Bellek Yonetimi

    /// Tek bir URL'nin onbellegini temizler.
    func removeImage(for urlString: String) {
        cache.removeObject(forKey: urlString as NSString)
    }

    /// Tum onbellegi temizler.
    func clearCache() {
        cache.removeAllObjects()
    }
}
