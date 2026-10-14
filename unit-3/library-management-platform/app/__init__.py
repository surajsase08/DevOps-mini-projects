from flask import Flask
from app.routes.api import api


def create_app():
    app = Flask(__name__)
    app.register_blueprint(api, url_prefix="/api")

    @app.route("/")
    def home():
        return {
            "message": "Welcome to the Library Management Platform",
            "api": "/api/books",
            "status": "running",
        }, 200

    @app.route("/health")
    def health():
        return {"status": "healthy"}, 200

    return app
