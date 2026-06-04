# ==============================================================================
# AKILLI SPORCU PERFORMANS TAKIP UYGULAMASI - VERI URETIM VE SIMULASYON BETIGI
# ==============================================================================
# Bu kod, yapay zeka modellerini test etmek ve veri tabanini beslemek amaciyla
# gercekci sensor (Ivmeolcer, Jiroskop, Nabiz) verileri uretir.

import json
import random
import time

def generate_athlete_telemetry(athlete_id, session_type="Running"):
    """
    Belirli bir sporcu ve antrenman tipi icin anlik sensor verisi simule eder.
    """
    timestamp = int(time.time())
    
    # Antrenman tipine gore gercekci nabiz ve hareket verisi uretimi
    if session_type == "Running":
        heart_rate = random.randint(140, 180)
        accel_x = round(random.uniform(1.2, 3.5), 3)
        accel_y = round(random.uniform(2.0, 5.0), 3)
        accel_z = round(random.uniform(-0.5, 0.8), 3)
    elif session_type == "HIIT":
        heart_rate = random.randint(150, 195)
        accel_x = round(random.uniform(2.5, 6.0), 3)
        accel_y = round(random.uniform(3.0, 7.5), 3)
        accel_z = round(random.uniform(-1.5, 2.0), 3)
    else: # Dinlenme veya hafif tempo
        heart_rate = random.randint(70, 110)
        accel_x = round(random.uniform(0.0, 0.5), 3)
        accel_y = round(random.uniform(0.8, 1.2), 3)
        accel_z = round(random.uniform(-0.1, 0.2), 3)

    payload = {
        "metadata": {
            "version": "1.0",
            "generator": "SmartAthlete Data Engine"
        },
        "telemetry": {
            "athlete_id": athlete_id,
            "session_type": session_type,
            "timestamp": timestamp,
            "biometrics": {
                "heart_rate_bpm": heart_rate,
                "blood_oxygen_pct": random.randint(95, 99)
            },
            "inertial_sensors": {
                "accelerometer_g": {"x": accel_x, "y": accel_y, "z": accel_z},
                "gyroscope_dps": {
                    "alpha": round(random.uniform(-180, 180), 1),
                    "beta": round(random.uniform(-180, 180), 1),
                    "gamma": round(random.uniform(-90, 90), 1)
                }
            }
        }
    }
    return payload

if __name__ == "__main__":
    print("--- Akilli Sporcu Performans Takip Uygulamasi ---")
    print("Simulasyon verileri uretiliyor...\n")
    
    # ATH-001 ID'li sporcu icin ornek bir kosu verisi uretelim
    sample_output = generate_athlete_telemetry(athlete_id="ATH-001", session_type="Running")
    
    # Uretilen veriyi ekrana şık bir formatta basalim
    print(json.dumps(sample_output, indent=2))
    print("\n[BASARILI] Simulasyon verisi uretildi ve test edilmeye hazir!")
