from flask import Blueprint

general_bp = Blueprint(
    "general_bp",
    __name__,
    static_folder="static",
    static_url_path="/general/static",
    template_folder="templates",
)

from project.general import views