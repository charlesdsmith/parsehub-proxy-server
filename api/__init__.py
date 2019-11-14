# models
from flask import Flask
from models import db
import os
from routes import app
basedir = os.path.abspath(os.path.dirname(__file__))

app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')

class Config(object):
    # ...
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False


def create_app():
    """Construct the core application."""

    db.init_app(app)
    app.config.from_object(Config)

    with app.app_context():
        print("MAPS",app.url_map)
        # Create tables for our models
        db.create_all()
        app.run()
        return app

if __name__ == "__main__":
    create_app()
