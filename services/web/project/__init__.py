from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import users, questions, questions_comments


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)

app.register_blueprint(users.users_bp)
app.register_blueprint(questions.questions_bp)
app.register_blueprint(questions_comments.questions_comments_bp)

@app.route('/')
def index():
    return "Main page"


