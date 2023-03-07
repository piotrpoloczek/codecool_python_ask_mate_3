from flask import render_template
from project.questions_comments import questions_comments_bp


@questions_comments_bp.get("/")
def home():
    return render_template("questions_comments/home.html")