from flask import Blueprint, request, jsonify

therapist_bp = Blueprint('therapist', __name__)

@therapist_bp.route('/dashboard', methods=['GET'])
def therapist_dashboard():
    return jsonify({"message": "Therapist dashboard data"})

@therapist_bp.route('/patients', methods=['GET'])
def therapist_patients():
    return jsonify({"patients": [{"id": 1, "name": "Patient A"}, {"id": 2, "name": "Patient B"}]})

@therapist_bp.route('/patient/<int:patient_id>', methods=['GET'])
def monitor_patient_progress(patient_id):
    return jsonify({"patient_id": patient_id, "progress": "Sample progress data"})

@therapist_bp.route('/adjust_plan', methods=['POST'])
def adjust_exercise_plan():
    data = request.json
    return jsonify({"message": "Exercise plan adjusted", "patient_id": data.get("patient_id")})

@therapist_bp.route('/notify', methods=['POST'])
def send_notifications():
    data = request.json
    return jsonify({"message": "Notification sent", "patient_id": data.get("patient_id")})
