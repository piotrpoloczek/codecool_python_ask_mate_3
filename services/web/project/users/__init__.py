from flask import Blueprint

users_bp = Blueprint(
    "users_bp",
    __name__,
    static_folder="static",
    static_url_path="/users/static",
    template_folder="templates",
    url_prefix="/users",
)

from project.users import views