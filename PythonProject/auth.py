from flask import Blueprint, jsonify, request
from models import db, User
from schema import UserSchema
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity

auth_bp = Blueprint("auth_bp", __name__)
user_schema = UserSchema()

# 📌 Register User
@auth_bp.route("/register", methods=["POST"])
def register_user():
    data = request.get_json()
    errors = user_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    if User.query.filter_by(username=data["username"]).first():
        return jsonify({"msg": "User already exists"}), 400

    new_user = User(username=data["username"])
    new_user.set_password(data["password"])
    new_user.role = data.get("role", "user")

    db.session.add(new_user)
    db.session.commit()
    return jsonify({"msg": "User created successfully"}), 201

# 📌 Login User
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data["username"]).first()

    if not user or not user.check_password(data["password"]):
        return jsonify({"msg": "Bad username or password"}), 401

    access_token = create_access_token(identity=user.username, additional_claims={"role": user.role})
    return jsonify(access_token=access_token), 200

# 📌 Protected Route (Example)
@auth_bp.route("/profile", methods=["GET"])
@jwt_required()
def profile():
    current_user = get_jwt_identity()
    return jsonify({"msg": f"Hello, {current_user}! This is a protected route."}), 200
