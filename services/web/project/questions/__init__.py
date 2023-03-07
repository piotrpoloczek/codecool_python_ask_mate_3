from flask import Blueprint

questions_bp = Blueprint(
    "questions_bp",
    __name__,
    static_folder="static",
    static_url_path="/questions/static",
    template_folder="templates/questions",
    url_prefix="/questions",
)

from project.questions import views