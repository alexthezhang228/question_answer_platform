'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-19 12:16:43
LastEditors: alexthezhang228 zhangy32@tcd.ie
LastEditTime: 2023-03-01 23:55:33
FilePath: /flask_project/blueprints/questions.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from flask import Blueprint, request, render_template, g, redirect, url_for
from .forms import QuestionForm, AnswerForm
from models import QuestionModel, AnswerModel
from exts import db
from decorates import login_required


bp = Blueprint('qa', __name__, url_prefix='/')


@bp.route('/')
def index():
    questions = QuestionModel.query.order_by(
        QuestionModel.create_time.desc()).all()

    return render_template('index.html', questions=questions)


@bp.route('/question/public', methods=['POST', 'GET'])
@login_required
def public_qa():
    if request.method == 'GET':
        return render_template('public_question.html')
    else:
        form = QuestionForm(request.form)
        title = form.title.data
        if form.validate():
            title = form.title.data
            content = form.content.data
            question = QuestionModel(
                title=title, content=content, author=g.user)
            db.session.add(question)
            db.session.commit()
            return redirect('/')
        else:
            # print(form.errors)
            return redirect(url_for('qa.public_qa'))


@bp.route('/qa/detail/<qa_id>')
def qa_detail(qa_id):
    question = QuestionModel.query.get(qa_id)
    # print(question.content)
    return render_template('details.html', question=question)


@bp.route('/anwser/public', methods=['POST'])
@login_required
def public_answer():
    form = AnswerForm(request.form)
    if form.validate():
        content = form.content.data
        question_id = form.question_id.data
        answer = AnswerModel(
            content=content, question_id=question_id, author_id=g.user.id)
        db.session.add(answer)
        db.session.commit()
        return redirect(url_for('qa.qa_detail', qa_id=question_id))
    else:
        return redirect(url_for('qa.qa_detail', qa_id=request.form.get('question_id')))
