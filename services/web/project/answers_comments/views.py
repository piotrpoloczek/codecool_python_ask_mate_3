from flask import render_template
from project.answers_comments import answers_comments_bp


@answers_comments_bp.get("/")
def home():
    return render_template("answers_comments/home.html")