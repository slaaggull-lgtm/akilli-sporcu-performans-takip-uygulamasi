import unittest
from InjuryRiskAnalyzer import InjuryRiskAnalyzer, AthleteSnapshot


class TestInjuryRiskAnalyzer(unittest.TestCase):

    def setUp(self):
        self.analyzer = InjuryRiskAnalyzer()

    def _make_snapshot(self, **kwargs) -> AthleteSnapshot:
        defaults = dict(
            athlete_id           = "TEST_01",
            age                  = 25,
            weekly_loads         = [400.0] * 28,
            hrv_values           = [70.0, 70.0, 70.0, 70.0, 70.0, 70.0, 70.0],
            resting_hr           = [50.0] * 7,
            sleep_scores         = [80.0] * 7,
            ground_contact_times = [235.0] * 10
        )
        defaults.update(kwargs)
        return AthleteSnapshot(**defaults)

    # ---- ACWR testleri -------------------------------------------- #

    def test_acwr_safe_zone_returns_low_risk(self):
        snap   = self._make_snapshot(weekly_loads=[400.0] * 28)
        report = self.analyzer.analyze(snap)
        self.assertLess(report.risk_score, 25.0,
                        "Dengeli yük → Düşük risk bekleniyor.")

    def test_acwr_overload_returns_high_risk(self):
        """Son 7 gün ani yük artışı — ACWR > 1.5 senaryosu."""
        loads  = [300.0] * 21 + [600.0] * 7
        snap   = self._make_snapshot(weekly_loads=loads)
        report = self.analyzer.analyze(snap)
        self.assertGreater(report.acwr, 1.5)
        self.assertIn(report.risk_label, ["Yüksek", "Kritik"])

    # ---- HRV testleri --------------------------------------------- #

    def test_hrv_crash_elevates_risk(self):
        """HRV %25 düşüşü → risk artmalı."""
        hrv    = [75.0, 75.0, 74.0, 73.0, 72.0, 71.0, 56.0]
        snap   = self._make_snapshot(hrv_values=hrv)
        report = self.analyzer.analyze(snap)
        self.assertGreater(report.hrv_drop_percent, 20.0)
        self.assertGreater(report.risk_score, 25.0)

    def test_stable_hrv_keeps_risk_low(self):
        hrv    = [72.0] * 7
        snap   = self._make_snapshot(hrv_values=hrv)
        report = self.analyzer.analyze(snap)
        self.assertLess(report.hrv_drop_percent, 5.0)

    # ---- GCT testleri --------------------------------------------- #

    def test_high_gct_adds_risk(self):
        gct    = [270.0] * 10
        snap   = self._make_snapshot(ground_contact_times=gct)
        report = self.analyzer.analyze(snap)
        self.assertGreater(report.gct_avg, 250.0)

    def test_normal_gct_no_gct_penalty(self):
        gct    = [230.0] * 10
        snap   = self._make_snapshot(ground_contact_times=gct)
        report = self.analyzer.analyze(snap)
        self.assertLessEqual(report.gct_avg, 250.0)

    # ---- Risk etiketi sınır testleri ------------------------------ #

    def test_critical_risk_label_above_75(self):
        loads  = [200.0] * 21 + [700.0] * 7
        hrv    = [80.0, 78.0, 75.0, 70.0, 60.0, 55.0, 50.0]
        snap   = self._make_snapshot(weekly_loads=loads, hrv_values=hrv)
        report = self.analyzer.analyze(snap)
        self.assertIn(report.risk_label, ["Yüksek", "Kritik"])

    def test_recommendations_not_empty(self):
        snap   = self._make_snapshot()
        report = self.analyzer.analyze(snap)
        self.assertGreater(len(report.recommendations), 0)

    # ---- Edge-case testleri --------------------------------------- #

    def test_insufficient_load_data_returns_neutral_acwr(self):
        snap   = self._make_snapshot(weekly_loads=[400.0, 400.0, 400.0])
        report = self.analyzer.analyze(snap)
        self.assertEqual(report.acwr, 1.0)

    def test_single_hrv_value_returns_zero_drop(self):
        snap   = self._make_snapshot(hrv_values=[70.0])
        report = self.analyzer.analyze(snap)
        self.assertEqual(report.hrv_drop_percent, 0.0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
