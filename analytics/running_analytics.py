import numpy as np

class RunningAnalytics:
    def __init__(self, age, gender, max_hr=None):
        self.age = age
        self.gender = gender # 'male' or 'female'
        self.max_hr = max_hr if max_hr else 220 - age

    def calculate_metrics(self, distance_km, duration_sec, heart_rate_avg, total_steps=None):
        """
        Calculates basic running metrics.
        """
        if duration_sec <= 0:
            return None

        # 1. Average Speed (km/h)
        avg_speed = (distance_km / duration_sec) * 3600

        # 2. Pace (min/km)
        pace = (duration_sec / 60) / distance_km

        # 3. Cadence (steps per minute)
        cadence = None
        if total_steps:
            cadence = (total_steps / duration_sec) * 60

        # 4. VO2 Max Estimation (Uth–Sørensen–Overgaard–Pedersen estimation)
        # VO2max = 15.3 x (HRmax / HRrest) -> modified for activity
        # Here we use a simpler clinical estimation: VO2max = 15 * (HRmax / HRavg) * intensity_factor
        # Or better: Firstbeat method approximation:
        intensity_ratio = heart_rate_avg / self.max_hr
        vo2_max = 0
        if distance_km > 0:
            # Cooper Test inspired approximation if distance is significant
            # VO2max = (distance_2200m - 504.9) / 44.73
            # But for general runs, we use METs calculation:
            speed_m_min = (distance_km * 1000) / (duration_sec / 60)
            vo2_max = (0.2 * speed_m_min) + (0.9 * speed_m_min * 0) + 3.5 # 0 grade
            
        return {
            "avg_speed_kmh": round(avg_speed, 2),
            "pace_minkm": round(pace, 2),
            "cadence_spm": round(cadence, 1) if cadence else None,
            "vo2_max_estimate": round(vo2_max, 2),
            "intensity_percentage": round(intensity_ratio * 100, 1)
        }

# Example usage for testing
if __name__ == "__main__":
    analyzer = RunningAnalytics(age=25, gender='male')
    # Use 5km run in 25 mins, 160 avg HR, 4500 steps
    results = analyzer.calculate_metrics(distance_km=5.0, duration_sec=1500, heart_rate_avg=160, total_steps=4500)
    print(f"Test Results: {results}")
