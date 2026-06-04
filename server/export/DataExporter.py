import csv
import json
import os
from datetime import datetime
from dataclasses import dataclass, asdict
from typing import Optional


@dataclass
class WorkoutRecord:
    workout_id: int
    athlete_id: str
    date: str
    workout_type: str
    duration_min: int
    avg_heart_rate: int
    calories_burned: float
    distance_km: Optional[float]
    avg_speed_kmh: Optional[float]
    avg_cadence_spm: Optional[int]
    vo2_max_estimate: Optional[float]
    hrv_rmssd: Optional[float]
    notes: str


class DataExporter:
    """
    Sporcu antrenman verilerini farklı formatlarda
    (CSV, JSON, Markdown Raporu) dışa aktaran sınıf.
    """

    def __init__(self, output_dir: str = "exports"):
        self.output_dir = output_dir
        os.makedirs(output_dir, exist_ok=True)

    # ------------------------------------------------------------------ #
    #  CSV Dışa Aktarma
    # ------------------------------------------------------------------ #

    def export_to_csv(
        self,
        records: list[WorkoutRecord],
        athlete_id: str
    ) -> str:
        """
        Antrenman kayıtlarını CSV dosyasına aktarır.

        Returns:
            str: Oluşturulan dosyanın yolu.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = f"{self.output_dir}/{athlete_id}_workouts_{timestamp}.csv"

        if not records:
            raise ValueError("Dışa aktarılacak kayıt bulunamadı.")

        fieldnames = list(asdict(records[0]).keys())

        with open(filename, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for record in records:
                writer.writerow(asdict(record))

        print(f"✅ CSV oluşturuldu: {filename}  ({len(records)} kayıt)")
        return filename

    # ------------------------------------------------------------------ #
    #  JSON Dışa Aktarma
    # ------------------------------------------------------------------ #

    def export_to_json(
        self,
        records: list[WorkoutRecord],
        athlete_id: str,
        pretty: bool = True
    ) -> str:
        """
        Antrenman kayıtlarını JSON dosyasına aktarır.

        Returns:
            str: Oluşturulan dosyanın yolu.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = f"{self.output_dir}/{athlete_id}_workouts_{timestamp}.json"

        payload = {
            "athlete_id"   : athlete_id,
            "exported_at"  : datetime.now().isoformat(),
            "total_records": len(records),
            "workouts"     : [asdict(r) for r in records]
        }

        with open(filename, "w", encoding="utf-8") as f:
            json.dump(payload, f, ensure_ascii=False,
                      indent=4 if pretty else None)

        print(f"✅ JSON oluşturuldu: {filename}  ({len(records)} kayıt)")
        return filename

    # ------------------------------------------------------------------ #
    #  Markdown Performans Raporu
    # ------------------------------------------------------------------ #

    def export_to_markdown_report(
        self,
        records: list[WorkoutRecord],
        athlete_id: str
    ) -> str:
        """
        Antrenman verilerinden okunabilir bir Markdown
        performans raporu oluşturur.

        Returns:
            str: Oluşturulan dosyanın yolu.
        """
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename  = f"{self.output_dir}/{athlete_id}_report_{timestamp}.md"

        stats = self._compute_summary_stats(records)

        lines = [
            f"# 📊 Performans Raporu — {athlete_id}",
            f"",
            f"**Oluşturma Tarihi:** {datetime.now().strftime('%d.%m.%Y %H:%M')}  ",
            f"**Toplam Antrenman:** {len(records)}  ",
            f"",
            f"---",
            f"",
            f"## 📈 Özet İstatistikler",
            f"",
            f"| Metrik | Değer |",
            f"|--------|-------|",
            f"| Toplam Süre | {stats['total_duration_min']} dakika |",
            f"| Toplam Kalori | {stats['total_calories']:.0f} kcal |",
            f"| Toplam Mesafe | {stats['total_distance_km']:.2f} km |",
            f"| Ort. Kalp Atışı | {stats['avg_heart_rate']:.0f} bpm |",
            f"| Ort. VO2 Max Tahmini | {stats['avg_vo2_max']:.1f} ml/kg/dk |",
            f"| En Uzun Antrenman | {stats['max_duration_min']} dakika |",
            f"",
            f"---",
            f"",
            f"## 🗓️ Antrenman Geçmişi",
            f"",
            f"| Tarih | Tür | Süre | Kalori | Ort. Nabız | Mesafe |",
            f"|-------|-----|------|--------|------------|--------|",
        ]

        for r in sorted(records, key=lambda x: x.date, reverse=True):
            lines.append(
                f"| {r.date} | {r.workout_type} | {r.duration_min} dk "
                f"| {r.calories_burned:.0f} kcal | {r.avg_heart_rate} bpm "
                f"| {f'{r.distance_km:.1f} km' if r.distance_km else '-'} |"
            )

        lines += [
            f"",
            f"---",
            f"",
            f"*Bu rapor Akıllı Sporcu Performans Takip Uygulaması tarafından otomatik oluşturulmuştur.*",
        ]

        with open(filename, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))

        print(f"✅ Markdown Raporu oluşturuldu: {filename}")
        return filename

    # ------------------------------------------------------------------ #
    #  Yardımcı: İstatistik Hesaplama
    # ------------------------------------------------------------------ #

    def _compute_summary_stats(self, records: list[WorkoutRecord]) -> dict:
        if not records:
            return {}

        durations  = [r.duration_min for r in records]
        calories   = [r.calories_burned for r in records]
        hr_values  = [r.avg_heart_rate for r in records]
        distances  = [r.distance_km for r in records if r.distance_km]
        vo2_values = [r.vo2_max_estimate for r in records if r.vo2_max_estimate]

        return {
            "total_duration_min"  : sum(durations),
            "total_calories"      : sum(calories),
            "total_distance_km"   : sum(distances),
            "avg_heart_rate"      : sum(hr_values) / len(hr_values),
            "avg_vo2_max"         : (sum(vo2_values) / len(vo2_values))
                                    if vo2_values else 0.0,
            "max_duration_min"    : max(durations),
        }


# ------------------------------------------------------------------ #
#  Hızlı demo
# ------------------------------------------------------------------ #
if __name__ == "__main__":
    sample_records = [
        WorkoutRecord(1,  "SPORCU_001", "2026-05-01", "Koşu",    45, 152, 480.0, 8.2,  10.9, 175, 47.5, 68.0, "Sabah koşusu"),
        WorkoutRecord(2,  "SPORCU_001", "2026-05-03", "Yürüyüş", 60, 118, 320.0, 6.0,  6.0,  115, None, 72.0, "Aktif dinlenme"),
        WorkoutRecord(3,  "SPORCU_001", "2026-05-05", "HIIT",    35, 171, 560.0, None, None, None, 49.2, 62.0, "Yüksek yoğunluk"),
        WorkoutRecord(4,  "SPORCU_001", "2026-05-07", "Koşu",    50, 158, 530.0, 9.1,  10.9, 173, 48.8, 65.0, ""),
        WorkoutRecord(5,  "SPORCU_001", "2026-05-09", "Bisiklet",70, 138, 610.0, 28.0, 24.0, None, 46.0, 70.0, "Düşük yoğunluk"),
    ]

    exporter = DataExporter(output_dir="exports")
    exporter.export_to_csv(sample_records,             "SPORCU_001")
    exporter.export_to_json(sample_records,            "SPORCU_001")
    exporter.export_to_markdown_report(sample_records, "SPORCU_001")
