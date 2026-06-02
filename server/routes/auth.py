from flask import Blueprint, request, jsonify

auth_bp = Blueprint('auth', __name__)


@auth_bp.route('/register', methods=['POST'])
def register():
    """
    Yeni kullanıcı kaydı.
    Beklenen JSON: {"email": "...", "password": "...", "name": "..."}
    """
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Veri bulunamadi"}), 400

    email = data.get('email', '')
    name = data.get('name', '')

    if not email or not name:
        return jsonify({"success": False, "message": "Email ve isim zorunlu"}), 400

    return jsonify({
        "success": True,
        "userId": "mock_user_123",
        "token": "mock_jwt_token_abc123",
        "message": f"{email} kaydi basarili"
    }), 201


@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Kullanici girisi.
    Beklenen JSON: {"email": "...", "password": "..."}
    """
    data = request.get_json()
    if not data:
        return jsonify({"success": False, "message": "Veri bulunamadi"}), 400

    email = data.get('email', '')
    password = data.get('password', '')

    if not email or not password:
        return jsonify({"success": False, "message": "Email ve sifre zorunlu"}), 400

    return jsonify({
        "success": True,
        "userId": "mock_user_123",
        "token": "mock_jwt_token_abc123",
        "email": email
    }), 200


@auth_bp.route('/logout', methods=['POST'])
def logout():
    return jsonify({"success": True, "message": "Cikis basarili"}), 200
