from flask import request, jsonify, session
# from app import app
from security import generate_hash_password, verify_password, is_valid_email
from models import db, User
from sqlalchemy import select
from flask_jwt_extended import create_access_token, create_refresh_token, get_jwt_identity

def register_service(name, email, password):
    try:
        if(is_valid_email(email)):
            pass
        else:
            return jsonify({"error":"invalid email address"}), 401
        print(User.query.all())
        hashed_password=generate_hash_password(password)
        # print(hashed_password)
        new_user = User(name=name, email=email, password=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"success":"created the user successfully"})
    except Exception as e:
        print(e)
        db.session.rollback()
        return jsonify({"error" : "Problems in registering the user."}), 500

def login_service(email, password):
    try:
        user = User.query.filter_by(email=email).all()
        print(user[0])
        hashed_password = user[0].password
        print(hashed_password)
        if(verify_password(password, hashed_password)):
            # session['user_id']=user[0].id
            access_token = create_access_token(identity=user[0].id)
            refresh_token = create_refresh_token(identity=user[0].id)
            print(session)
            return jsonify(access_token=access_token, refresh_token=refresh_token), 201
        return jsonify({"error":"Authentication error"}), 401
    except Exception as e:
        print(e)
        return jsonify({"error" : "Problems in logging in the user"}), 500

def profile_service(user_id):
    try:
        if user_id is None:
            return jsonify({"error":"you are not logged in"}), 401
        user = User.query.filter_by(id=user_id).all()
        if user is None:
            return jsonify({"error":"user not found"}), 404
        user_details=[user[0].name, user[0].id, user[0].email]
        # print(user_details)
        return jsonify({"User ID":f"{user_details[1]}", "User Name":f"{user_details[0]}", "User Email" : f"{user_details[2]}"}), 201
    except Exception as e:
        print(e)
        return jsonify({"error":"server error"}), 500

def logout_service(user_id):
    try:
        user = User.query.filter_by(id=user_id).all()
        # session.pop("user_id")
        return jsonify({"Success": f"User {user[0].id} has been logged out successfully"}), 200
    except Exception as e:
        print(e)
        return jsonify({"error" : "Problems in logging out the user"}), 500
        
def refresh_service():
    try:
        id = get_jwt_identity()
        if id is None:
            return jsonify({"error":"please login again"}), 401
        new_access_token = create_access_token(id)
        return jsonify(access_token=new_access_token), 200
    except Exception as e:
        return jsonify({"error":"encountered an error in the backend"}), 500