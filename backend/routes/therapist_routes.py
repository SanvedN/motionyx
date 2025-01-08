from flask import Blueprint, request, jsonify
from datetime import datetime
from config.db import get_therapist_schema , mongo
from bson.objectid import ObjectId

therapist_bp = Blueprint('therapist', __name__)

@therapist_bp.route('/signup', methods=['POST'])
def signup():
    data = request.get_json()
    schema = get_therapist_schema()

    try:
        # Validate incoming data
        for key in schema:
            if key not in data:
                return jsonify({"error": f"Missing field: {key}"}), 400

        dob = datetime.strptime(data['dob'], '%Y-%m-%d')

        # Prepare the new therapist record
        therapist_data = {
            "name": data["name"],
            "age": data["age"],
            "dob": dob,
            "email": data["email"],
            "password": data["password"],
            "gender": data["gender"],
            "qualification": data.get("qualification"),
            "expertise": data.get("expertise"),
            "YearOfExperience": data.get("YearOfExperience"),

        }

        # Insert the document and get the inserted ID
        result = mongo.db.therapist.insert_one(therapist_data)

        # Add the inserted ID to the response, converting ObjectId to string
        therapist_data["_id"] = str(result.inserted_id)
        return jsonify({
            "message": "Signup successful" , "therapist_data" : therapist_data
        })

    except KeyError as e:
        return jsonify({"error": f"Missing field: {str(e)}"}), 400
    except ValueError as e:
        return jsonify({"error": f"Invalid data format: {str(e)}"}), 400
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@therapist_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.get_json()

        email = data.get("email")
        password = data.get("password")

        if not email or not password:
            return jsonify({"error": "Email and password are required"}), 400

        # Fetch the user from the database
        therapist = mongo.db.therapist.find_one({"email": email})

        if not therapist:
            return jsonify({"error": "User not found"}), 404

        # Verify the password
        if not(therapist["password"], password):
            return jsonify({"error": "Invalid credentials"}), 401

        # Convert the ObjectId to a string for the response
        therapist["_id"] = str(therapist["_id"])

        # Mask sensitive data in the response
        therapist.pop("password")

        return jsonify({
            "message": "Login successful",
            "therapist": therapist,
             "token" : str(therapist["_id"])
        }), 200

    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

@therapist_bp.route('/dashboard', methods=['GET'])
def therapist_dashboard():
    print(request.headers.get('token'))
    try:
        id = request.headers.get('token')

        if not id:
            return jsonify({"error": "not logged in"}), 400
        
        therapist = mongo.db.therapist.find_one({"_id": ObjectId(id)})
        print("here!!!")
        
        if not therapist:
            print("here!!!!!")
            return jsonify({"error": "User not found"}), 404

        therapist["_id"] = str(therapist["_id"])
        therapist.pop("password")
        therapist.pop("_id")
        print("here!!!!")

        return jsonify({
                "message": "therapist Details",
                "therapist": therapist
            }), 200

    except Exception as e:
        print("not here!!!!")
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500
    
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
