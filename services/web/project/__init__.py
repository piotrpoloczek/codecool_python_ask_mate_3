from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from project import (
    users, 
    questions, 
    questions_comments,
    answers,
    answers_comments,
    general,
)


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


app.register_blueprint(general.general_bp)
app.register_blueprint(users.users_bp)
app.register_blueprint(questions.questions_bp)
app.register_blueprint(questions_comments.questions_comments_bp)
app.register_blueprint(answers_comments.answers_comments_bp)
app.register_blueprint(answers.answers_bp)
