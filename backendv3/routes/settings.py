from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required

settings_bp = Blueprint("settings", __name__)

@settings_bp.route('/', methods=['GET', 'POST'])
@jwt_required()
def settings():
    if request.method == 'GET':
        # Trả về dữ liệu settings
        return jsonify({"settings": "User settings"})
    elif request.method == 'POST':
        # Cập nhật dữ liệu settings
        return jsonify({"message": "Settings updated"})
