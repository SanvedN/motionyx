from flask import Flask
from routes import user, theRapist, patient

app = Flask(__name__)

# Register Blueprints
app.register_blueprint(user.user_bp, url_prefix='/user')
app.register_blueprint(theRapist.therapist_bp, url_prefix='/theRapist')
app.register_blueprint(patient.patient_bp, url_prefix='/patient')

if __name__ == '__main__':
    app.run(debug=True)
