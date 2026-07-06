import os
from flask import Flask
from flask_migrate import Migrate
from config import Config, DevelopmentConfig, TestConfig
from app.models import db
from app.routers.categories import categories_bp
from app.routers.questions import questions_bp
from app.routers.responses import responses_bp


def create_app():
    app = Flask(__name__)

    flask_mode = os.environ.get("FLASK_ENV", "development")

    config_class = {
        "development": DevelopmentConfig,
        "production": Config,
        "testing": TestConfig,
    }.get(flask_mode)

    app.config.from_object(config_class)

    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    app.register_blueprint(questions_bp, url_prefix="/questions")
    app.register_blueprint(responses_bp, url_prefix="/responses")
    app.register_blueprint(categories_bp, url_prefix="/categories")

    return app
