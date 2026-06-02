from flask import Flask
from flask_cors import CORS
from routes.auth import auth_bp
from routes.workout import workout_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(auth_bp, url_prefix='/auth')
app.register_blueprint(workout_bp, url_prefix='/api')


@app.route('/')
def health():
    return {"status": "ok", "message": "Akilli Sporcu API calisiyor"}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
