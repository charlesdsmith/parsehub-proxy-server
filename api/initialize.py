# models
from flask import Flask
import os
from routes import app

def create_app():
    """Construct the core application."""

    with app.app_context():
        app.run()
        return app

if __name__ == "__main__":
    create_app()
