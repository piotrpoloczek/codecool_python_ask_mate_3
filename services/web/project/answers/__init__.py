from flask import Blueprint

answers_bp = Blueprint(
    "answers_bp",
    __name__,
    static_folder="static",
    static_url_path="/answers/static",
    template_folder="templates",
    url_prefix="/answers",
)

from project.answers import views