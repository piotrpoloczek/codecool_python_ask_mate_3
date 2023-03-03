from flask import (
    Flask,
    jsonify,
    send_from_directory,
    request,
    render_template,
    jsonify,
)
from flask_sqlalchemy import SQLAlchemy
from werkzeug.utils import secure_filename
import os
import math
import project.data.queries as queries
from project.api import api_get


app = Flask(__name__)
app.config.from_object("project.config.Config")
db = SQLAlchemy(app)


    
@app.route('/')
def index():
    return "Main page"