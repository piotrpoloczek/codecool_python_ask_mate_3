from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import users


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

app.register_blueprint(users.users_bp)

@app.route('/')
def index():
    return "Main page"


