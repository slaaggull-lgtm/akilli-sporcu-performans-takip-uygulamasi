import numpy as np
from dataclasses import dataclass
from typing import Optional

@dataclass
class AthleteSnapshot:
    athlete_id: str
    age: int
    weekly_loads: list[float]       # Son 28 günlük yük geçmişi
    hrv_values: list[float]         # Son 7 günlük HRV (RMSSD, ms)
    resting_hr: list[float]         # Son 7 günlük dinlenik nabız
    sleep_scores: list[float]       # 0-100 arası uyku kalitesi
    ground_contact_times: list[float]  # ms cinsinden GCT değerleri

@dataclass
class RiskReport:
    athlete_id: str
    acwr: float
    hrv_drop_percent: float
    resting_hr_trend: float
    gct_avg: float
    risk_score: float               # 0-100 arası genel risk skoru
    risk_label: str                 # "Düşük", "Orta", "Yüksek", "Kritik"
    recommendations: list[str]


class InjuryRiskAnalyzer:
    """
    Sporcu biyometrik ve kinematik verilerini analiz ederek
    sakatlık riskini hesaplayan motor sınıf.
    """

    # ACWR güvenli bölge eşikleri (literatür: Gabbett, 2016)
    ACWR_LOW    = 0.80
    ACWR_HIGH   = 1.30
    ACWR_DANGER = 1.50

    # HRV düşüş eşikleri (% olarak baseline'dan sapma)
    HRV_WARNING  = 0.10   # %10 düşüş → uyarı
    HRV_CRITICAL = 0.20   # %20 düşüş → kritik

    # GCT güvenli üst sınır (ms)
    GCT_THRESHOLD = 250.0

    def analyze(self, snapshot: AthleteSnapshot) -> RiskReport:
        acwr         = self._compute_acwr(snapshot.weekly_loads)
        hrv_drop     = self._compute_hrv_drop(snapshot.hrv_values)
        hr_trend     = self._compute_hr_trend(snapshot.resting_hr)
        gct_avg      = float(np.mean(snapshot.ground_contact_times)) \
                       if snapshot.ground_contact_times else 230.0

        risk_score   = self._compute_risk_score(acwr, hrv_drop, hr_trend, gct_avg)
        risk_label   = self._classify_risk(risk_score)
        recommendations = self._generate_recommendations(
            acwr, hrv_drop, hr_trend, gct_avg, risk_label
        )

        return RiskReport(
            athlete_id      = snapshot.athlete_id,
            acwr            = round(acwr, 3),
            hrv_drop_percent= round(hrv_drop * 100, 1),
            resting_hr_trend= round(hr_trend, 2),
            gct_avg         = round(gct_avg, 1),
            risk_score      = round(risk_score, 1),
            risk_label      = risk_label,
            recommendations = recommendations
        )

    # ------------------------------------------------------------------ #
    #  Metrik Hesaplama Metodları
    # ------------------------------------------------------------------ #

    def _compute_acwr(self, loads: list[float]) -> float:
        """Akut:Kronik Yük Oranı — pencere: 7 akut / 28 kronik gün."""
        if len(loads) < 7:
            return 1.0
        acute   = np.mean(loads[-7:])
        chronic = np.mean(loads[-28:]) if len(loads) >= 28 else np.mean(loads)
        return float(acute / chronic) if chronic > 0 else 1.0

    def _compute_hrv_drop(self, hrv_values: list[float]) -> float:
        """Baseline HRV ortalamasına göre son değerin düşüş oranı."""
        if len(hrv_values) < 2:
            return 0.0
        baseline = float(np.mean(hrv_values[:-1]))
        latest   = hrv_values[-1]
        return max(0.0, (baseline - latest) / baseline) if baseline > 0 else 0.0

    def _compute_hr_trend(self, hr_values: list[float]) -> float:
        """Dinlenik nabızdaki lineer trend eğimi (+ = artış = kötü)."""
        if len(hr_values) < 3:
            return 0.0
        x = np.arange(len(hr_values), dtype=float)
        coeffs = np.polyfit(x, hr_values, 1)
        return float(coeffs[0])   # Eğim

    def _compute_risk_score(
        self, acwr: float, hrv_drop: float,
        hr_trend: float, gct_avg: float
    ) -> float:
        """
        Ağırlıklı kompozit risk skoru (0-100).
        Ağırlıklar: ACWR %40, HRV %30, HR Trend %15, GCT %15
        """
        # ACWR bileşeni
        if acwr > self.ACWR_DANGER:
            acwr_score = 100.0
        elif acwr > self.ACWR_HIGH:
            acwr_score = 60.0 + (acwr - self.ACWR_HIGH) / \
                         (self.ACWR_DANGER - self.ACWR_HIGH) * 40.0
        elif acwr < self.ACWR_LOW:
            acwr_score = 20.0
        else:
            acwr_score = 10.0

        # HRV bileşeni
        hrv_score = min(hrv_drop / self.HRV_CRITICAL, 1.0) * 100.0

        # HR trend bileşeni
        hr_score  = min(max(hr_trend * 10.0, 0.0), 100.0)

        # GCT bileşeni
        gct_score = min(max((gct_avg - self.GCT_THRESHOLD) / 50.0, 0.0), 1.0) * 100.0

        return 0.40 * acwr_score + 0.30 * hrv_score + \
               0.15 * hr_score  + 0.15 * gct_score

    @staticmethod
    def _classify_risk(score: float) -> str:
        if score >= 75: return "Kritik"
        if score >= 50: return "Yüksek"
        if score >= 25: return "Orta"
        return "Düşük"

    @staticmethod
    def _generate_recommendations(
        acwr: float, hrv_drop: float,
        hr_trend: float, gct_avg: float,
        label: str
    ) -> list[str]:
        recs = []
        if label == "Kritik":
            recs.append("⛔ Yüksek yoğunluklu antrenman 48-72 saat ertelenmeli.")
            recs.append("🛏️ Uyku önceliği: 9+ saat hedeflenmelidir.")
        if acwr > 1.30:
            recs.append(f"📉 ACWR {acwr:.2f} — haftalık antrenman hacmi %20 azaltılmalı.")
        if hrv_drop > 0.10:
            recs.append(f"💓 HRV %{hrv_drop*100:.0f} düştü — Zone 1-2 aktif toparlanma önerilir.")
        if hr_trend > 0.5:
            recs.append("❤️ Dinlenik nabız artış eğiliminde — overtraining riski izleniyor.")
        if gct_avg > 250:
            recs.append(f"🦵 GCT {gct_avg:.0f}ms — pliyometrik egzersiz ve kadans çalışması önerilir.")
        if not recs:
            recs.append("✅ Tüm metrikler normal aralıkta. Antrenman planına devam edebilirsiniz.")
        return recs


# ------------------------------------------------------------------ #
#  Hızlı test çalıştırması
# ------------------------------------------------------------------ #
if __name__ == "__main__":
    sample = AthleteSnapshot(
        athlete_id           = "SPORCU_001",
        age                  = 24,
        weekly_loads         = [420, 450, 480, 390, 510, 530, 480,
                                460, 490, 505, 470, 440, 460, 490,
                                520, 480, 500, 510, 490, 470, 460,
                                480, 500, 515, 520, 550, 580, 600],
        hrv_values           = [72, 70, 68, 65, 63, 61, 56],
        resting_hr           = [48, 49, 49, 50, 51, 52, 54],
        sleep_scores         = [82, 79, 75, 71, 68, 65, 63],
        ground_contact_times = [235, 240, 248, 255, 262, 258, 265]
    )

    analyzer = InjuryRiskAnalyzer()
    report   = analyzer.analyze(sample)

    print("=" * 50)
    print(f"  Sporcu ID  : {report.athlete_id}")
    print(f"  ACWR       : {report.acwr}")
    print(f"  HRV Düşüşü : %{report.hrv_drop_percent}")
    print(f"  HR Trend   : {report.resting_hr_trend} bpm/gün")
    print(f"  Ort. GCT   : {report.gct_avg} ms")
    print(f"  Risk Skoru : {report.risk_score} / 100")
    print(f"  Risk Etiketi: {report.risk_label}")
    print("\n  Öneriler:")
    for r in report.recommendations:
        print(f"    {r}")
    print("=" * 50)
