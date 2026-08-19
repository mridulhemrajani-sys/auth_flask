from flask import request, jsonify, session
# from app import app
from security import generate_hash_password, verify_password, is_valid_email
from models import db, User
from sqlalchemy import select

def register_service(name, email, password):
    try:
        if(is_valid_email(email)):
            pass
        else:
            return jsonify({"error":"invalid email address"})
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
            session['user_id']=user[0].id
            print(session)
            return jsonify({"success":"User authenicated"}), 201
        return jsonify({"error":"Authentication error"}), 500
    except Exception as e:
        print(e)
        return jsonify({"error" : "Problems in logging in the user"}), 500

def profile_service(user_id):
    try:
        user = User.query.filter_by(id=user_id).all()
        user_details=[user[0].name, user[0].id, user[0].email]
        # print(user_details)
        return jsonify({"User ID":f"{user_details[1]}", "User Name":f"{user_details[0]}", "User Email" : f"{user_details[2]}"})
    except Exception as e:
        print(e)
        return jsonify({"error":"user not found"})

def logout_service(user_id):
    try:
        user = User.query.filter_by(id=user_id).all()
        session.pop("user_id")
        return jsonify({"Success": f"User {user[0].id} has been logged out successfully"})
    except Exception as e:
        print(e)
        return jsonify({"error" : "Problems in logging out the user"}), 500
        
