
from flask import Flask
from settings import DevelpoConfig
from flask_migrate import Migrate
from apps.models import Users,Worker
from exts import db
from apps.views.api_bp import api_bp

def create_app():
    app = Flask(__name__)
    app.config.from_object(DevelpoConfig)
    db.init_app(app)

    migrate = Migrate()
    migrate.init_app(app, db)

    app.register_blueprint(api_bp)
    print(app.url_map)
    return app