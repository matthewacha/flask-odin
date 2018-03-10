"""assigns a constant users the Blueprint class, imports views"""
from flask import Blueprint

users = Blueprint('users', __name__, template_folder="templates")

from . import views
