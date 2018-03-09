"""import dependencies"""
from flask import Flask

#import app blueprints
from app.users import users as users_blueprint

APP = Flask(__name__)

"""register app blueprints"""
APP.register_blueprint(users_blueprint)

#"""register api blueprints"""
