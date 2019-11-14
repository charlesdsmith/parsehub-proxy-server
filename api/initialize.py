# models
from flask import Flask
import os
from routes import app

basedir = os.path.abspath(os.path.dirname(__file__))


def create_app():
    """Construct the core application."""

    with app.app_context():
<<<<<<< HEAD
        # Create tables for our models
=======
>>>>>>> b3c92a8c1eb52e30ef325ba9c16da644339bd9bb
        app.run()
        return app

if __name__ == "__main__":
    create_app()
