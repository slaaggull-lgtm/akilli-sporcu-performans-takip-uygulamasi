"""
Antrenman Optimizasyon Modulu

Uc farkli strateji ile sporcular icin optimal haftalik antrenman yukunu hesaplar:

  Strateji 1: ACWR Kural Motoru — hizli, yorumlanabilir
  Strateji 2: Evrimsel Algoritma — yuksek kapasiteli kesef
  Strateji 3: XGBoost ML Modeli — en yuksek kisellestirme
"""

import random
import numpy as np


# ==============================================================
# STRATEJi 1: ACWR Kural Motoru (Acute:Chronic Workload Ratio)
# ==============================================================

def compute_acwr(weekly_loads, acute_window=7, chronic_window=28):
    """
    Akut:Kronik Yuk Orani (ACWR) hesaplar.

    ACWR = Akut yuk ortalamasi / Kronik yuk ortalamasi
    Guvenli bant: 0.8 – 1.3
    > 1.5 ise yaralanma riski yuksek
    < 0.8 ise yuk azaltilabilir

    Parametreler:
        weekly_loads (list): Gunluk antrenman yuk listesi (en az 28 eleman)
        acute_window (int): Akut pencere genisligi (gun), varsayilan 7
        chronic_window (int): Kronik pencere genisligi (gun), varsayilan 28

    Donus degeri:
        float: ACWR degeri
    """
    if len(weekly_loads) < chronic_window:
        return 1.0  # Yetersiz veri — nötr oran döndür

    acute = sum(weekly_loads[-acute_window:]) / acute_window
    chronic = sum(weekly_loads[-chronic_window:]) / chronic_window

    return round(acute / chronic, 3) if chronic > 0 else 1.0


def apply_load_constraint(base_load, acwr):
    """
    ACWR degerine gore antrenman yukunu ayarlar.

    Parametreler:
        base_load (float): Planlanan temel antrenman yuku
        acwr (float): Hesaplanan ACWR degeri

    Donus degeri:
        float: Duzeltilmis antrenman yuku
    """
    if acwr > 1.5:
        # Yuksek yaralanma riski — yuku %40 azalt
        adjusted = base_load * 0.60
        reason = "Yuksek yaralanma riski (ACWR>1.5), yuk azaltildi"
    elif acwr > 1.3:
        # Dikkatli bolge — hafif azalt
        adjusted = base_load * 0.85
        reason = "Dikkat bolgesi (ACWR 1.3-1.5), yuk hafifce azaltildi"
    elif acwr < 0.8:
        # Dusuk yuk — arttirilabilir
        adjusted = base_load * 1.15
        reason = "Dusuk yuk bolgesi (ACWR<0.8), yuk arttiriildi"
    else:
        # Guvenli bolge — degistirme
        adjusted = base_load
        reason = "Guvenli bolge (ACWR 0.8-1.3), yuk degismedi"

    return {
        "original_load": base_load,
        "adjusted_load": round(adjusted, 1),
        "acwr": acwr,
        "reason": reason
    }


# ==============================================================
# STRATEJi 2: Evrimsel Algoritma (Genetik Yaklasim)
# ==============================================================

def fitness(program, athlete):
    """
    Bir antrenman programinin uygunlugunu (fitness skorunu) hesaplar.
    Yuksek skor = sporcu icin daha iyi program.

    Parametreler:
        program (list): Her elemanin {"intensity": 0-1, "duration": dakika}
                        oldugu 7 gunluk program
        athlete (dict): {"chronic_load": float} iceren sporcu verisi

    Donus degeri:
        float: 0-1 arasi uygunluk skoru
    """
    total_load = sum(day["intensity"] * day["duration"] for day in program)
    recovery_days = sum(1 for day in program if day["intensity"] == 0)

    # Hedef yuk — kronik yukun %10 ustunde
    target_load = athlete.get("chronic_load", 400) * 1.1
    load_score = max(0, 1 - abs(total_load - target_load) / max(target_load, 1))

    # En az 2 dinlenme gunu olmali
    recovery_score = min(recovery_days / 2, 1.0)

    # Agirlikli puan: %60 yuk dengesi, %40 toparlanma
    return round(0.60 * load_score + 0.40 * recovery_score, 4)


def crossover(parent_a, parent_b):
    """
    Iki antrenman programini tek noktali caprazlama ile birlestir.

    Parametreler:
        parent_a (list): 1. ebeveyn program (7 gunluk)
        parent_b (list): 2. ebeveyn program (7 gunluk)

    Donus degeri:
        list: Caprazlama sonucu yeni program
    """
    if len(parent_a) <= 1:
        return parent_a[:]
    point = random.randint(1, len(parent_a) - 1)
    return parent_a[:point] + parent_b[point:]


def mutate(program, rate=0.1):
    """
    Programi rastgele mutasyona ugratir.

    Parametreler:
        program (list): Mutasyona ugrayacak program
        rate (float): Her gunun mutasyon olasiligi (0-1)

    Donus degeri:
        list: Mutasyona ugramis yeni program
    """
    return [
        {**day, "intensity": round(random.uniform(0, 1), 2)}
        if random.random() < rate else day
        for day in program
    ]


def run_genetic_optimization(athlete, generations=50, population_size=20):
    """
    Genetik algoritmayi calistirarak en iyi haftalik programi bulur.

    Parametreler:
        athlete (dict): Sporcu ozellikleri
        generations (int): Nesil sayisi
        population_size (int): Her nesildeki birey sayisi

    Donus degeri:
        dict: En iyi program ve fitness skoru
    """
    # Baslangic populasyonu: rastgele 7 gunluk programlar
    population = [
        [{"intensity": round(random.uniform(0, 1), 2), "duration": random.randint(30, 90)}
         for _ in range(7)]
        for _ in range(population_size)
    ]

    best_program = None
    best_score = -1

    for gen in range(generations):
        # Her bireyin fitness'ini hesapla
        scored = [(prog, fitness(prog, athlete)) for prog in population]
        scored.sort(key=lambda x: x[1], reverse=True)

        if scored[0][1] > best_score:
            best_score = scored[0][1]
            best_program = scored[0][0]

        # En iyi %50'yi secilimle aliko
        survivors = [s[0] for s in scored[:population_size // 2]]

        # Caprazlama ve mutasyonla yeni nesil olustur
        new_population = survivors[:]
        while len(new_population) < population_size:
            a, b = random.sample(survivors, 2)
            child = mutate(crossover(a, b))
            new_population.append(child)

        population = new_population

    return {
        "best_program": best_program,
        "fitness_score": best_score,
        "generations_run": generations
    }


# ==============================================================
# STRATEJi 3: XGBoost ML Modeli
# ==============================================================

def build_features(athlete):
    """
    Sporcu ozelliklerinden ML model giris vektoru olusturur.

    Parametreler:
        athlete (dict): Sporcu verisi

    Donus degeri:
        numpy.ndarray: (1, 6) boyutlu ozellik vektoru
    """
    return np.array([[
        athlete.get("age", 25),
        athlete.get("chronic_load", 400),
        athlete.get("acwr", 1.0),
        athlete.get("hrv", 65),           # Heart Rate Variability (ms)
        athlete.get("sleep_score", 70),   # 0-100 arasi uyku kalitesi
        athlete.get("days_to_match", 7)   # Bir sonraki maca/yarismaya kalan gun
    ]])


def predict_optimal_load_mock(athlete):
    """
    XGBoost modeli yokken kural tabanli tahmin uretir.
    Gercek projede: model.predict(build_features(athlete)) kullanilir.

    Parametreler:
        athlete (dict): Sporcu verisi

    Donus degeri:
        float: Optimal haftalik antrenman yuku
    """
    base = athlete.get("chronic_load", 400)
    acwr = athlete.get("acwr", 1.0)
    hrv = athlete.get("hrv", 65)
    sleep = athlete.get("sleep_score", 70)

    # HRV ve uyku kalitesine gore yuk ayarla
    recovery_factor = (hrv / 80 + sleep / 100) / 2  # 0-1 arasi

    # ACWR'a gore basal multiplier
    if acwr > 1.3:
        multiplier = 0.85
    elif acwr < 0.8:
        multiplier = 1.15
    else:
        multiplier = 0.95 + 0.1 * recovery_factor

    return round(base * multiplier, 1)


# ==============================================================
# KARSILASTIRMALI DEMO
# ==============================================================

if __name__ == "__main__":
    # Ornek sporcu profili
    sample_athlete = {
        "age": 26,
        "chronic_load": 450.0,   # Son 28 gunluk ortalama gunluk yuk
        "acwr": 1.15,
        "hrv": 62.0,             # RMSSD — ms cinsinden
        "sleep_score": 72,
        "days_to_match": 5
    }

    # Ornek gunluk yuk gecmisi (28 gun)
    daily_loads = [350, 380, 0, 420, 410, 0, 390,
                   400, 430, 0, 450, 440, 0, 410,
                   420, 460, 0, 480, 450, 0, 430,
                   440, 470, 0, 490, 460, 0, 450]

    print("=" * 50)
    print("STRATEJi 1: ACWR Kural Motoru")
    print("=" * 50)
    acwr = compute_acwr(daily_loads)
    result1 = apply_load_constraint(500, acwr)
    for k, v in result1.items():
        print(f"  {k}: {v}")

    print("\n" + "=" * 50)
    print("STRATEJi 2: Evrimsel Algoritma")
    print("=" * 50)
    result2 = run_genetic_optimization(sample_athlete, generations=30, population_size=10)
    print(f"  En iyi fitness skoru: {result2['fitness_score']}")
    print(f"  Nesil sayisi: {result2['generations_run']}")

    print("\n" + "=" * 50)
    print("STRATEJi 3: XGBoost (Kural Bazli Mock)")
    print("=" * 50)
    result3 = predict_optimal_load_mock(sample_athlete)
    print(f"  Optimal haftalik yuk: {result3}")
    print(f"  Ozellik vektoru: {build_features(sample_athlete)}")
