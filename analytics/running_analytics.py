"""
Kosu Analitigi Modulu
Giyilebilir sensorlerden gelen verilerle temel kos performans metriklerini hesaplar.
"""


class RunningAnalytics:
    """
    Kosu antrenmani verilerini analiz eden sinif.

    Parametreler:
        age (int): Sporcunun yasi
        gender (str): 'male' veya 'female'
        max_hr (int): Maksimum kalp atisi (belirtilmezse 220-yas formuluyle hesaplanir)
    """

    def __init__(self, age, gender, max_hr=None):
        self.age = age
        self.gender = gender
        self.max_hr = max_hr if max_hr else 220 - age

    def calculate_metrics(self, distance_km, duration_sec, heart_rate_avg, total_steps=None):
        """
        Kosu metriklerini hesaplar.

        Parametreler:
            distance_km (float): Kat edilen mesafe (km)
            duration_sec (int): Sure (saniye)
            heart_rate_avg (int): Ortalama kalp atisi (bpm)
            total_steps (int): Toplam adim sayisi (opsiyonel)

        Donus degeri:
            dict: Hesaplanan metrikler
        """
        if duration_sec <= 0:
            return None

        # Ortalama hiz (km/saat)
        avg_speed_kmh = (distance_km / duration_sec) * 3600

        # Pace (dakika/km) — kosucular icin standart tempo gostergesi
        pace_min_km = (duration_sec / 60) / distance_km

        # Kadans (adim/dakika) — adim verisi varsa hesapla
        cadence_spm = None
        if total_steps and total_steps > 0:
            cadence_spm = (total_steps / duration_sec) * 60

        # VO2 Max tahmini — METs formuluyle (klinik kabul goren)
        # Formul: VO2Max = (0.2 * hiz_m_dak) + 3.5
        speed_m_per_min = (distance_km * 1000) / (duration_sec / 60)
        vo2_max_estimate = (0.2 * speed_m_per_min) + 3.5

        # Antrenman yogunluk orani — maks kalp atisinin yuzdesi
        intensity_pct = heart_rate_avg / self.max_hr

        # Kalp atisi zonu (1-5)
        hr_zone = self._calculate_hr_zone(intensity_pct)

        return {
            "avg_speed_kmh": round(avg_speed_kmh, 2),
            "pace_min_km": round(pace_min_km, 2),
            "cadence_spm": round(cadence_spm, 1) if cadence_spm else None,
            "vo2_max_estimate": round(vo2_max_estimate, 2),
            "intensity_percentage": round(intensity_pct * 100, 1),
            "hr_zone": hr_zone,
            "max_hr_used": self.max_hr
        }

    def _calculate_hr_zone(self, intensity_ratio):
        """
        Kalp atisi zonunu hesaplar (1-5 arasi).
        1: Cok dusuk (<%60), 2: Dusuk (60-70%), 3: Orta (70-80%),
        4: Yuksek (80-90%), 5: Maksimum (>%90)
        """
        if intensity_ratio < 0.60:
            return 1
        elif intensity_ratio < 0.70:
            return 2
        elif intensity_ratio < 0.80:
            return 3
        elif intensity_ratio < 0.90:
            return 4
        else:
            return 5

    def calculate_weekly_summary(self, sessions):
        """
        Haftalik antrenman ozetini hesaplar.

        Parametreler:
            sessions (list): Her biri calculate_metrics ciktisi olan antrenman listesi

        Donus degeri:
            dict: Haftalik ozet
        """
        if not sessions:
            return {}

        valid = [s for s in sessions if s is not None]
        if not valid:
            return {}

        return {
            "session_count": len(valid),
            "avg_speed_kmh": round(sum(s["avg_speed_kmh"] for s in valid) / len(valid), 2),
            "avg_vo2_max": round(sum(s["vo2_max_estimate"] for s in valid) / len(valid), 2),
            "avg_intensity_pct": round(sum(s["intensity_percentage"] for s in valid) / len(valid), 1),
            "dominant_zone": max(
                set(s["hr_zone"] for s in valid),
                key=lambda z: sum(1 for s in valid if s["hr_zone"] == z)
            )
        }


# ---- TEST (dosyayi dogrudan calistirarak kontrol edebilirsin) ----
if __name__ == "__main__":
    analyzer = RunningAnalytics(age=25, gender="female")

    result = analyzer.calculate_metrics(
        distance_km=5.2,
        duration_sec=1680,   # 28 dakika
        heart_rate_avg=152,
        total_steps=4200
    )

    print("=== KOSU ANALiZ SONUCLARI ===")
    for key, value in result.items():
        print(f"{key}: {value}")
