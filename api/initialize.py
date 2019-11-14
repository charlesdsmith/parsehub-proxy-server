# models
from flask import Flask
import os
from routes import app

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    """Construct the core application."""

    with app.app_context():
        # Create tables for our models
        app.run()
        return app

if __name__ == "__main__":
    create_app()
