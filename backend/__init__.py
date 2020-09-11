# Package Requirements
import os
from flask import Flask
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_migrate import Migrate

# Local Requirements
from .models import db
from .config import Config
from .auth import auth
from .api.users import user
from .api.boats import boat
from .api.vehicles import vehicle


# Declarations
app = Flask(__name__)
app.config.from_object(Config)
CORS(app)
jwt = JWTManager(app)
db.init_app(app)
migrate = Migrate(app, db)


# Blueprint Registration
app.register_blueprint(auth, url_prefix='/auth')
app.register_blueprint(user, url_prefix='/api/users')
app.register_blueprint(boat, url_prefix='/api/boats')
app.register_blueprint(vehicle, url_prefix='/api/vehicles')


# Default Routing
@app.route('/', defaults={'path': ''})
@app.route('/<path>')
def react_root(path):
    return app.send_static_file('index.html')
