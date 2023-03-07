from flask import Blueprint

questions_comments_bp = Blueprint(
    "questions_comments_bp",
    __name__,
    static_folder="static",
    static_url_path="/questions_comments/static",
    template_folder="templates",
    url_prefix="/questions_comments",
)

from project.questions_comments import views