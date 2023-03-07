from flask import render_template
from project.questions import questions_bp


@questions_bp.get("/")
def home():
    return render_template("home.html")