from flask import Flask
from flask_jwt_extended import JWTManager
from config import Config
from database import db  # Import đối tượng db từ database.py
from routes.auth import auth_bp
from routes.dashboard import dashboard_bp
from routes.map import map_bp
from routes.settings import settings_bp

app = Flask(__name__)
app.config.from_object(Config)

# Khởi tạo các extension với app
db.init_app(app)
jwt = JWTManager(app)

# Đăng ký các Blueprint
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(dashboard_bp, url_prefix="/dashboard")
app.register_blueprint(map_bp, url_prefix="/map")
app.register_blueprint(settings_bp, url_prefix="/settings")

# Tạo các bảng trong cơ sở dữ liệu nếu chưa có
with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
