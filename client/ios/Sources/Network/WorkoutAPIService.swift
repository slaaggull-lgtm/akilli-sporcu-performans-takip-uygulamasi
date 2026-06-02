import Foundation

// MARK: - Veri Modelleri

/// Antrenman plani modeli — API'den gelen JSON'u eslestirir
struct WorkoutPlan: Codable {
    let id: Int
    let title: String
    let description: String
    let duration: Int          // Dakika cinsinden sure
    let exercises: [Exercise]
}

/// Tekil egzersiz modeli
struct Exercise: Codable {
    let id: Int
    let name: String
    let sets: Int
    let reps: Int
    let restSeconds: Int

    enum CodingKeys: String, CodingKey {
        case id, name, sets, reps
        case restSeconds = "rest_seconds"  // JSON'daki snake_case -> Swift camelCase
    }
}

/// Sensor verisi modeli — giyilebilir cihazdan gelen anlık data
struct SensorData: Codable {
    let athleteId: String
    let heartRate: Int
    let steps: Int
    let timestamp: String
    let latitude: Double?
    let longitude: Double?
}

// MARK: - API Hata Tipleri

/// Hata durumlarini tanimlayan enum
enum APIError: Error, LocalizedError {
    case invalidURL
    case noData
    case decodingError(String)
    case serverError(Int)
    case networkError(String)

    var errorDescription: String? {
        switch self {
        case .invalidURL:
            return "Gecersiz URL."
        case .noData:
            return "Sunucudan veri alinamadi."
        case .decodingError(let message):
            return "Veri cozumleme hatasi: \(message)"
        case .serverError(let code):
            return "Sunucu hatasi: HTTP \(code)"
        case .networkError(let message):
            return "Ag baglantisi hatasi: \(message)"
        }
    }
}

// MARK: - API Servisi

/// REST API islemlerini yoneten singleton servis sinifi
class WorkoutAPIService {

    static let shared = WorkoutAPIService()

    // Gercek API adresiyle degistir (ornekl: Flask server adresi)
    private let baseURL = "https://api.example.com"

    private let session: URLSession

    private init() {
        let config = URLSessionConfiguration.default
        config.timeoutIntervalForRequest = 30   // Istek zaman asimi: 30 saniye
        config.timeoutIntervalForResource = 60  // Kaynak zaman asimi: 60 saniye
        self.session = URLSession(configuration: config)
    }

    // MARK: - Tum Antrenman Planlarini Getir

    /// GET /api/workoutData — Tum antrenman planlarini getirir
    func fetchWorkoutPlans(completion: @escaping (Result<[WorkoutPlan], APIError>) -> Void) {
        guard let url = URL(string: "\(baseURL)/api/workoutData") else {
            completion(.failure(.invalidURL))
            return
        }

        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        // Gercek uygulamada: request.setValue("Bearer \(token)", forHTTPHeaderField: "Authorization")

        performRequest(request: request, completion: completion)
    }

    // MARK: - Belirli Antrenman Planini Getir

    /// GET /api/workoutData/:id — Tek bir plani getirir
    func fetchWorkoutPlan(id: Int, completion: @escaping (Result<WorkoutPlan, APIError>) -> Void) {
        guard let url = URL(string: "\(baseURL)/api/workoutData/\(id)") else {
            completion(.failure(.invalidURL))
            return
        }

        var request = URLRequest(url: url)
        request.httpMethod = "GET"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        performRequest(request: request, completion: completion)
    }

    // MARK: - Sensor Verisi Gonder

    /// POST /api/sensorData — Giyilebilir sensordan gelen veriyi gonderir
    func sendSensorData(_ data: SensorData, completion: @escaping (Result<Bool, APIError>) -> Void) {
        guard let url = URL(string: "\(baseURL)/api/sensorData") else {
            completion(.failure(.invalidURL))
            return
        }

        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")

        do {
            request.httpBody = try JSONEncoder().encode(data)
        } catch {
            completion(.failure(.decodingError("Veri kodlanamadi: \(error.localizedDescription)")))
            return
        }

        session.dataTask(with: request) { _, response, error in
            DispatchQueue.main.async {
                if let error = error {
                    completion(.failure(.networkError(error.localizedDescription)))
                    return
                }
                if let httpResponse = response as? HTTPURLResponse,
                   (200...299).contains(httpResponse.statusCode) {
                    completion(.success(true))
                } else {
                    completion(.failure(.serverError(0)))
                }
            }
        }.resume()
    }

    // MARK: - Genel Istek Fonksiyonu

    private func performRequest<T: Decodable>(
        request: URLRequest,
        completion: @escaping (Result<T, APIError>) -> Void
    ) {
        session.dataTask(with: request) { data, response, error in
            DispatchQueue.main.async {

                // Ag hatasi
                if let error = error {
                    completion(.failure(.networkError(error.localizedDescription)))
                    return
                }

                // HTTP durum kodu kontrolu
                if let httpResponse = response as? HTTPURLResponse {
                    guard (200...299).contains(httpResponse.statusCode) else {
                        completion(.failure(.serverError(httpResponse.statusCode)))
                        return
                    }
                }

                // Veri kontolu
                guard let data = data else {
                    completion(.failure(.noData))
                    return
                }

                // JSON cozumleme
                do {
                    let decoded = try JSONDecoder().decode(T.self, from: data)
                    completion(.success(decoded))
                } catch {
                    completion(.failure(.decodingError(error.localizedDescription)))
                }
            }
        }.resume()
    }
}

// MARK: - Mock Veri Testi

/// Gercek API olmadan JSON cozumlemeyi test eder
func testWithMockData() {
    let mockJSON = """
    [
        {
            "id": 1,
            "title": "Ust Vucut Antrenman",
            "description": "Gogus, sirt ve omuz egzersizleri",
            "duration": 60,
            "exercises": [
                { "id": 1, "name": "Bench Press", "sets": 4, "reps": 10, "rest_seconds": 90 },
                { "id": 2, "name": "Pull-Up", "sets": 3, "reps": 8, "rest_seconds": 60 }
            ]
        }
    ]
    """.data(using: .utf8)!

    do {
        let plans = try JSONDecoder().decode([WorkoutPlan].self, from: mockJSON)
        print("Mock veri basariyla cozumlendi: \(plans.first?.title ?? "?")")
        print("Egzersiz sayisi: \(plans.first?.exercises.count ?? 0)")
    } catch {
        print("Hata: \(error)")
    }
}
