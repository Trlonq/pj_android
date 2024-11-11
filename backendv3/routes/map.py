from flask import Blueprint, jsonify
from flask_jwt_extended import jwt_required

map_bp = Blueprint("map", __name__)

@map_bp.route('/', methods=['GET'])
@jwt_required()
def get_map_data():
    # Trả về dữ liệu bản đồ
    return jsonify({"data": "Map data"})
