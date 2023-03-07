from flask import Blueprint

answers_comments_bp = Blueprint(
    "answers_comments_bp",
    __name__,
    static_folder="static",
    static_url_path="/answers_comments/static",
    template_folder="templates",
    url_prefix="/answers_comments",
)

from project.answers_comments import views