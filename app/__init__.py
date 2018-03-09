"""import dependencies"""
from flask import Flask

"""Initialise app"""
app = Flask(__name__)

"""register app blueprints"""
from app.users import users as users_blueprint
app.register_blueprint(users_blueprint)

"""register api blueprints"""
