from flask import render_template
from project.users import users_bp


@users_bp.get("/")
def home():
    return render_template("users/home.html")