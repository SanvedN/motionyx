from flask import Blueprint, request, jsonify

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/dashboard', methods=['GET'])
def patient_dashboard():
    return jsonify({"message": "Patient dashboard data"})

@patient_bp.route('/daily_plan', methods=['GET'])
def daily_exercise_plan():
    return jsonify({"exercise_plan": "Sample exercise plan"})

@patient_bp.route('/start_session', methods=['POST'])
def start_exercise_session():
    return jsonify({"message": "Exercise session started"})

@patient_bp.route('/real_time_feedback', methods=['POST'])
def real_time_feedback():
    return jsonify({"message": "Feedback processed"})

@patient_bp.route('/session_complete', methods=['POST'])
def session_complete():
    return jsonify({"message": "Session completed"})

@patient_bp.route('/progress', methods=['GET'])
def view_weekly_progress():
    return jsonify({"progress": "Sample weekly progress data"})

@patient_bp.route('/request_adjustment', methods=['POST'])
def request_plan_adjustment():
    data = request.json
    return jsonify({"message": "Adjustment request sent", "details": data})
