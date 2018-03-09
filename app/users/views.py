"""import dependencies"""
from flask import render_template, url_for
from . import users

@users.route('/', methods=['GET'])
def index():
    """endpoint for landing page """
    return "Hello world"
