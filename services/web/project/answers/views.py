from flask import render_template
from project.answers import answers_bp


@answers_bp.get("/")
def home():
    return render_template("answers/home.html")