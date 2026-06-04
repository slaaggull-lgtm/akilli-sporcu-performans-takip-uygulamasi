markdown# 📤 Veri Dışa Aktarma Modülü (Data Export Module)

Sporcu antrenman verilerini CSV, JSON ve Markdown raporu
formatlarında dışa aktaran backend modülü.

## 📁 Dosya Yapısı
server/export/
├── DataExporter.py    # Dışa aktarma motoru
├── export_routes.py   # FastAPI router (/export endpoint'leri)
└── README.md

## 🚀 Endpoint'ler

### `POST /export/generate`
Antrenman kayıtlarını belirtilen formatta dışa aktarır.

**Request Body:**
```json
{
  "athlete_id": "SPORCU_001",
  "format": "csv",
  "workouts": [
    {
      "workout_id": 1,
      "athlete_id": "SPORCU_001",
      "date": "2026-05-01",
      "workout_type": "Koşu",
      "duration_min": 45,
      "avg_heart_rate": 152,
      "calories_burned": 480.0,
      "distance_km": 8.2
    }
  ]
}
```

**Response:** İndirilebilir dosya (`Content-Disposition: attachment`)

### `GET /export/formats`
Desteklenen formatları listeler.

## ⚙️ Kurulum

```bash
pip install fastapi uvicorn
uvicorn export_routes:router --reload
```

## 📊 Desteklenen Formatlar

| Format | MIME Tipi | Kullanım |
|--------|-----------|----------|
| CSV | text/csv | Excel / Sheets analizi |
| JSON | application/json | API entegrasyonu |
| Markdown | text/markdown | Okunabilir rapor |
