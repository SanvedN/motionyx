from flask import Blueprint, request, jsonify

user_bp = Blueprint('user', __name__)

@user_bp.route('/login', methods=['POST'])
def login():
    data = request.json
    return jsonify({"message": "Login successful", "user_type": data.get("user_type")})

@user_bp.route('/signup', methods=['POST'])
def signup():
    data = request.json
    return jsonify({"message": "Signup successful"})
