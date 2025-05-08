from flask import Flask

def create_app():
    """Application factory pattern for initializing the Flask app."""
    app = Flask(__name__)

    # Register routes from routes.py
    from .routes import main
    app.register_blueprint(main)

    return app
