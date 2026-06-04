"""
FastAPI router: /export endpoint'leri.
Sporcu verilerini CSV veya JSON olarak indirilebilir
dosya formatında döndürür.
"""

from fastapi import APIRouter, HTTPException, Query
from fastapi.responses import FileResponse
from pydantic import BaseModel
from typing import Optional
import os

from DataExporter import DataExporter, WorkoutRecord

router = APIRouter(prefix="/export", tags=["Data Export"])
exporter = DataExporter(output_dir="exports")

# ------------------------------------------------------------------ #
#  Pydantic Şemaları
# ------------------------------------------------------------------ #

class WorkoutRecordDTO(BaseModel):
    workout_id       : int
    athlete_id       : str
    date             : str
    workout_type     : str
    duration_min     : int
    avg_heart_rate   : int
    calories_burned  : float
    distance_km      : Optional[float] = None
    avg_speed_kmh    : Optional[float] = None
    avg_cadence_spm  : Optional[int]   = None
    vo2_max_estimate : Optional[float] = None
    hrv_rmssd        : Optional[float] = None
    notes            : str = ""


class ExportRequest(BaseModel):
    athlete_id : str
    workouts   : list[WorkoutRecordDTO]
    format     : str  # "csv" | "json" | "markdown"


# ------------------------------------------------------------------ #
#  Endpoint'ler
# ------------------------------------------------------------------ #

@router.post(
    "/generate",
    summary="Antrenman verilerini dışa aktar",
    response_description="İndirilebilir dosya"
)
async def generate_export(request: ExportRequest):
    """
    Gönderilen antrenman kayıtlarını belirtilen formatta
    (csv / json / markdown) dışa aktarır ve indirilebilir
    bir dosya olarak döndürür.
    """
    if not request.workouts:
        raise HTTPException(status_code=400, detail="Dışa aktarılacak kayıt yok.")

    if request.format not in ("csv", "json", "markdown"):
        raise HTTPException(
            status_code=422,
            detail="Geçersiz format. 'csv', 'json' veya 'markdown' kullanın."
        )

    records = [
        WorkoutRecord(
            workout_id       = w.workout_id,
            athlete_id       = w.athlete_id,
            date             = w.date,
            workout_type     = w.workout_type,
            duration_min     = w.duration_min,
            avg_heart_rate   = w.avg_heart_rate,
            calories_burned  = w.calories_burned,
            distance_km      = w.distance_km,
            avg_speed_kmh    = w.avg_speed_kmh,
            avg_cadence_spm  = w.avg_cadence_spm,
            vo2_max_estimate = w.vo2_max_estimate,
            hrv_rmssd        = w.hrv_rmssd,
            notes            = w.notes
        )
        for w in request.workouts
    ]

    try:
        if request.format == "csv":
            filepath = exporter.export_to_csv(records, request.athlete_id)
            media    = "text/csv"
        elif request.format == "json":
            filepath = exporter.export_to_json(records, request.athlete_id)
            media    = "application/json"
        else:
            filepath = exporter.export_to_markdown_report(records, request.athlete_id)
            media    = "text/markdown"

    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    if not os.path.exists(filepath):
        raise HTTPException(status_code=500, detail="Dosya oluşturulamadı.")

    return FileResponse(
        path         = filepath,
        media_type   = media,
        filename     = os.path.basename(filepath)
    )


@router.get(
    "/formats",
    summary="Desteklenen dışa aktarma formatlarını listele"
)
async def list_formats():
    return {
        "supported_formats": [
            {"id": "csv",      "label": "CSV Elektronik Tablo",  "extension": ".csv"},
            {"id": "json",     "label": "JSON Veri Dosyası",     "extension": ".json"},
            {"id": "markdown", "label": "Markdown Performans Raporu", "extension": ".md"},
        ]
    }
