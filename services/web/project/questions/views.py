from flask import Flask, render_template, request, redirect, url_for
from project.questions import questions_bp


@questions_bp.route('/add_question', methods = ["POST", "GET"])
def add_question():
    if request.method == "POST":
        question = request.form
        #id = sql_manager.add_question(question)
        return redirect(url_for('question', id = id))
    else:
        return render_template('add_question.html')
   