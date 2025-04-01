from flask import Flask
from flask_cors import CORS, cross_origin
import os

def create_app():
    app = Flask(__name__)
    CORS(app, resources={r"/*": {"origins": "*"}})
    
    

    

    

    from app.api.routes import api_blueprint
    app.register_blueprint(api_blueprint)
    app.config['CORS_HEADERS'] = 'Content-Type'

    return app