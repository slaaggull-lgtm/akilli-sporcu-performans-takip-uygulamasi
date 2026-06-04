import unittest

class RunningAnalytics:
    def __init__(self, age, gender):
        self.age = age
        self.gender = gender
        self.max_hr = 220 - age

    def calculate_metrics(self, distance_km, duration_sec, heart_rate_avg, total_steps):
        if duration_sec <= 0 or distance_km <= 0 or total_steps <= 0:
            return None
        
        avg_speed_kmh = (distance_km / duration_sec) * 3600
        pace_minkm = (duration_sec / 60) / distance_km
        cadence_spm = (total_steps / duration_sec) * 60
        
        # Karvonen Formülü ile Antrenman Yoğunluk Skoru Hesabı
        hr_reserve = self.max_hr - 60  # Dinlenik nabız 60 varsayılmıştır
        intensity_pct = ((heart_rate_avg - 60) / hr_reserve) * 100
        
        # VO2 Max Tahmin Formülasyonu
        vo2_max_estimate = 15.3 * (self.max_hr / max(heart_rate_avg, 1))

        return {
            "avg_speed_kmh": round(avg_speed_kmh, 2),
            "pace_minkm": round(pace_minkm, 2),
            "cadence_spm": round(cadence_spm, 1),
            "intensity_percentage": round(intensity_pct, 1),
            "vo2_max_estimate": round(vo2_max_estimate, 2)
        }

class TestRunningAnalyticsPipeline(unittest.TestCase):
    def setUp(self):
        """Test ortamını hazırlar ve örnek verileri yükler"""
        self.engine = RunningAnalytics(age=24, gender="male")
        self.valid_payload = {
            "distance_km": 10.0,
            "duration_sec": 3000, # 50 dakika
            "heart_rate_avg": 155,
            "total_steps": 8500
        }

    def test_nominal_performance_calculation(self):
        """Standart bir koşu senaryosunun matematiksel doğruluğunu test eder"""
        result = self.engine.calculate_metrics(**self.valid_payload)
        
        self.assertIsNotNone(result)
        self.assertEqual(result["avg_speed_kmh"], 12.0)
        self.assertEqual(result["pace_minkm"], 5.0)
        self.assertAlmostEqual(result["cadence_spm"], 170.0, places=1)
        self.assertTrue(40.0 <= result["vo2_max_estimate"] <= 60.0)

    def test_boundary_zero_division_safety(self):
        """Sıfıra bölünme ve kritik girdi hatalarına karşı sistem direncini test eder"""
        bad_payload = self.valid_payload.copy()
        bad_payload["duration_sec"] = 0
        
        result = self.engine.calculate_metrics(**bad_payload)
        self.assertNone(result, "Sıfır süreli antrenman null dönmelidir, sistem çökmemelidir.")

    def test_physiological_anomaly_handling(self):
        """Aşırı yüksek veya imkansız fizyolojik verilerin durumunu test eder"""
        result = self.engine.calculate_metrics(5.0, 1200, heart_rate_avg=240, total_steps=3000)
        self.assertTrue(result["intensity_percentage"] > 100.0)

if __name__ == "__main__":
    unittest.main()
