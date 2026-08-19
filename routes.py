from flask import request, jsonify, Blueprint, session
# from app import app
# import bcrypt
from services import register_service, login_service, profile_service, logout_service

from models import User, db

main = Blueprint('main', __name__)

@main.route("/register", methods = ['POST'])
def register():
    """
    User Registration
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - name
            - email
            - password
          properties:
            name:
              type: string
              example: John Doe
            email:
              type: string
              example: john@example.com
            password:
              type: string
              example: securepassword123
    responses:
      200:
        description: User created successfully
      400:
        description: Missing or invalid JSON body
      500:
        description: Internal server error during registration
    """
    data=request.get_json()
    if not data:
        return jsonify({"error" : "Missing/Invalid JSON body."})
    name = data.get('name')
    email = data.get('email')
    # print(email)
    password = data.get('password')
    if not name or not email or not password:
        return jsonify({"error":"One of the required fields is missing"})
    return register_service(name, email, password)

@main.route("/login", methods = ['POST'])
def login():
    """
    User Login
    ---
    tags:
      - Authentication
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - email
            - password
          properties:
            email:
              type: string
              example: john@example.com
            password:
              type: string
              example: securepassword123
    responses:
      201:
        description: User authenticated successfully
      500:
        description: Authentication error or server issues
    """
    data = request.get_json()
    if not data:
        return jsonify({"error" : "Missing/Invalid JSON body."})
    email = data.get('email')
    password = data.get('password')
    return login_service(email, password)

@main.route("/profile", methods = ['GET'])
def profile():
    """
    Get User Profile
    ---
    tags:
      - User Actions
    responses:
      200:
        description: User details retrieved successfully
        schema:
          type: object
          properties:
            User ID:
              type: string
            User Name:
              type: string
            User Email:
              type: string
      500:
        description: User not found or session expired
    """
    user_id=session.get('user_id')
    return profile_service(user_id)

@main.route("/logout", methods = ['GET'])
def logout():
    """
    User Logout
    ---
    tags:
      - Authentication
    responses:
      200:
        description: User logged out successfully
      500:
        description: Logout processing errors
    """
    user_id=session.get('user_id')
    return logout_service(user_id)
    