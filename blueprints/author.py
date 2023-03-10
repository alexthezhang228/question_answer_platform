'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-19 12:16:37
LastEditors: alexthezhang228 110424337+alexthezhang228@users.noreply.github.com
LastEditTime: 2023-03-10 21:25:10
FilePath: /flask_project/blueprints/author.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from werkzeug.security import generate_password_hash, check_password_hash
from exts import mail, db
from flask_mail import Message
import random
from models import EmailCaptchaModel, UserModel
from .forms import RegisterForm, LoginForm

bp = Blueprint('author', __name__, url_prefix='/author')


@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = UserModel.query.filter_by(email=email).first()
            if not user:
                # print('email does not exist')
                # return 'user doen not exist'
                return redirect(url_for('author.register'))
            if check_password_hash(user.password, password):
                session['user_id'] = user.id
                # return 'go to main page'
                return redirect('/')
            else:
                # return 'wrong password'
                return redirect(url_for('author.login'))

        else:
            # print(form.errors)
            return 'wrong emaai oor cde'
            # return redirect(url_for('author/login'))


@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    else:
        form = RegisterForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            user = UserModel(email=email, username=username,
                             password=generate_password_hash(password))
            db.session.add(user)
            db.session.commit()
            # return 'success register!'
            return redirect(url_for('author.login'))
        else:
            # print(form.errors)
            return redirect(url_for('author.register'))


@bp.route('/captcha/email')
def get_email_captcha():
    email = request.args.get('email')
    if email is not None:
        code = str(random.randint(1111, 9999))
        message = Message(subject='email test send code', recipients=[
            email], body=f'this is a test message to generate code,  code is {code}')
        mail.send(message)
        email_captcha = EmailCaptchaModel(email=email, captcha=code)
        db.session.add(email_captcha)
        db.session.commit()
        return jsonify({'code': 200, 'message': '', 'data': None})
    else:
        return 'Invalid email'


@bp.route('/mail/test')
def main_test():
    message = Message(subject='email test', recipients=[
                      'yijingzhang228@gmail.com'], body='this is a test message')
    mail.send(message)

    return 'send successfully!'


@bp.route('/logout')
def logout():
    session.clear()
    return redirect('/')
