from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token
from werkzeug.security import generate_password_hash, check_password_hash
from models import User
from database import db

auth_bp = Blueprint("auth", __name__)

# Endpoint đăng ký
@auth_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Kiểm tra xem email và password có được cung cấp không
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Kiểm tra xem người dùng đã tồn tại chưa
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "User already exists"}), 400

    # Tạo người dùng mới và mã hóa mật khẩu
    new_user = User(email=email, password=generate_password_hash(password))
    db.session.add(new_user)
    db.session.commit()

    return jsonify({"message": "User registered successfully"}), 201

# Endpoint đăng nhập
@auth_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')

    # Kiểm tra xem email và password có được cung cấp không
    if not email or not password:
        return jsonify({"message": "Email and password are required"}), 400

    # Lấy thông tin người dùng từ cơ sở dữ liệu
    user = User.query.filter_by(email=email).first()

    # Kiểm tra người dùng và xác thực mật khẩu
    if not user or not check_password_hash(user.password, password):
        return jsonify({"message": "Invalid email or password"}), 401

    # Tạo JWT token cho người dùng
    access_token = create_access_token(identity=user.id)
    return jsonify({"access_token": access_token}), 200
