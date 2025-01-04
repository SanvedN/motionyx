from flask import Flask , jsonify
from routes import patient_routes, therapist_routes
from config.db import init_db

app = Flask(__name__)

init_db(app)

# Register Blueprints
app.register_blueprint(therapist_routes.therapist_bp, url_prefix='/therapist')
app.register_blueprint(patient_routes.patient_bp, url_prefix='/patient')

@app.route('/')
def home():
    return "Welcome to the application!"

if __name__ == '__main__':
    app.run(debug=True , port = 8080)
