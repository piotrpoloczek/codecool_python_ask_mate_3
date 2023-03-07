from flask import render_template
from project.general import general_bp


@general_bp.get("/")
def home():
    return render_template("general/home.html")