from flask import Blueprint, request, jsonify

workout_bp = Blueprint('workout', __name__)

# Örnek veri deposu (gerçek projede Firebase/SQLite olur)
SAMPLE_WORKOUTS = [
    {
        "id": 1,
        "userId": "mock_user_123",
        "date": "2026-05-28",
        "type": "Kosu",
        "duration_min": 45,
        "avg_heart_rate": 145,
        "calories": 380,
        "steps": 6200,
        "distance_km": 5.2,
        "notes": "Sabah kosusu, iyi hissettim"
    },
    {
        "id": 2,
        "userId": "mock_user_123",
        "date": "2026-05-29",
        "type": "Yuzme",
        "duration_min": 60,
        "avg_heart_rate": 132,
        "calories": 520,
        "steps": 0,
        "distance_km": 1.8,
        "notes": "Havuz antremani"
    }
]

SAMPLE_SENSOR_DATA = []


@workout_bp.route('/workoutData', methods=['GET'])
def get_workouts():
    """Kullanicinin tum antrenman verilerini dondurur."""
    return jsonify({
        "success": True,
        "count": len(SAMPLE_WORKOUTS),
        "workouts": SAMPLE_WORKOUTS
    }), 200


@workout_bp.route('/workoutData', methods=['POST'])
def add_workout():
    """
    Yeni antrenman verisi ekler.
    Beklenen JSON: {"type": "...", "duration_min": ..., "avg_heart_rate": ..., ...}
    """
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Veri bulunamadi"}), 400

    new_id = len(SAMPLE_WORKOUTS) + 1
    new_workout = {"id": new_id, "userId": "mock_user_123", **data}
    SAMPLE_WORKOUTS.append(new_workout)

    return jsonify({
        "success": True,
        "message": "Antrenman eklendi",
        "id": new_id,
        "data": new_workout
    }), 201


@workout_bp.route('/sensorData', methods=['POST'])
def add_sensor_data():
    """
    Giyilebilir sensorden gelen anlık veriyi alir.
    Beklenen JSON: {"athleteId": "...", "heart_rate": ..., "steps": ..., "timestamp": "..."}
    """
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Veri bulunamadi"}), 400

    SAMPLE_SENSOR_DATA.append(data)

    return jsonify({
        "success": True,
        "message": "Sensor verisi alindi",
        "received": data
    }), 201


@workout_bp.route('/sensorData', methods=['GET'])
def get_sensor_data():
    """Alinan tum sensor verilerini dondurur."""
    return jsonify({
        "success": True,
        "count": len(SAMPLE_SENSOR_DATA),
        "data": SAMPLE_SENSOR_DATA
    }), 200


@workout_bp.route('/performance/summary', methods=['GET'])
def get_performance_summary():
    """Kullanicinin ozet performans verilerini dondurur."""
    return jsonify({
        "success": True,
        "summary": {
            "total_workouts": len(SAMPLE_WORKOUTS),
            "total_calories": sum(w.get("calories", 0) for w in SAMPLE_WORKOUTS),
            "avg_heart_rate": round(
                sum(w.get("avg_heart_rate", 0) for w in SAMPLE_WORKOUTS) / len(SAMPLE_WORKOUTS), 1
            ),
            "total_distance_km": sum(w.get("distance_km", 0) for w in SAMPLE_WORKOUTS)
        }
    }), 200
