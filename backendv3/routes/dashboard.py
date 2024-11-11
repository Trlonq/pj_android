from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

dashboard_bp = Blueprint("dashboard", __name__)

@dashboard_bp.route('/', methods=['GET'])
@jwt_required()
def get_dashboard():
    # Trả về dữ liệu dashboard
    return jsonify({"data": "Dashboard data"})
