import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL",
                                        "postgresql://avnadmin:AVNS_K5PEAARi4daVtaQ1PHB@potholedb-trlonq.d.aivencloud.com:24953/defaultdb?sslmode=require")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretkey")
    JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "jwtsecretkey")
