from flask import Blueprint, request, jsonify
from datetime import datetime
from config.db import get_patient_schema , mongo

patient_bp = Blueprint('patient', __name__)

@patient_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    schema = get_patient_schema()

    try:
        # Validate incoming data
        for key in schema:
            if key not in data:
                return jsonify({"error": f"Missing field: {key}"}), 400

        dob = datetime.strptime(data['dob'], '%Y-%m-%d')

        # Prepare the new patient record
        patient_data = {
            "name": data["name"],
            "age": data["age"],
            "dob": dob,
            "email": data["email"],
            "password": data["password"],
            "gender": data["gender"],
            "medicalHistory": data.get("medicalHistory", []),
            "currentSymptoms": data.get("currentSymptoms", []),
        }

        # Insert the document and get the inserted ID
        result = mongo.db.patient.insert_one(patient_data)

        # Add the inserted ID to the response, converting ObjectId to string
        patient_data["_id"] = str(result.inserted_id)
        return jsonify({
            "message": "Signup successful" , "patient_data" : patient_data
        })

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    

@patient_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Fetch the user from the database
        patient = mongo.db.patient.find_one({"email": email})

        if not patient:
            return jsonify({"error": "User not found"}), 404

        # Verify the password
        if not(patient["password"], password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Convert the ObjectId to a string for the response
        patient["_id"] = str(patient["_id"])

        # Mask sensitive data in the response
        patient.pop("password")

        return jsonify({
            "message": "Login successful",
            "patient": patient
        }), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

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
