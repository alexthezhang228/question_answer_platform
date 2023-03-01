'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-22 19:47:20
LastEditors: alexthezhang228 zhangy32@tcd.ie
LastEditTime: 2023-03-01 23:48:16
FilePath: /flask_project/blueprints/forms.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
import wtforms
from wtforms.validators import Email, Length, EqualTo, InputRequired
from models import UserModel, EmailCaptchaModel
from exts import db


class RegisterForm(wtforms.Form):
    email = wtforms.StringField(
        validators=[Email(message='wrong email format')])
    code = wtforms.StringField(
        validators=[Length(min=4, max=4, message='Wrong code!')])
    username = wtforms.StringField(
        validators=[Length(min=3, max=20, message='wrong username format')])
    password = wtforms.StringField(
        validators=[Length(min=3, max=20, message='wrong passsword format')])
    password_confirm = wtforms.StringField(validators=[EqualTo('password')])

    # 1.  if email was registered

    def validate_email(self, field):
        email = field.data
        # print(email)
        user = UserModel.query.filter_by(email=email).first()
        if user:
            raise wtforms.ValidationError(
                message='the email has already registered.')

    # 2. if code is correct
    def validate_code(self, field):
        code = field.data
        email = self.email.data
        email_model = EmailCaptchaModel.query.filter_by(email=email).first()
        if not email_model:
            raise wtforms.ValidationError(message='wrong email or wrong code')
        code_model = EmailCaptchaModel.query.filter_by(
            email=email, captcha=code).first()
        if not code_model:
            raise wtforms.ValidationError(message='wrong email or wrong code')

        db.session.delete(code_model)
        db.session.commit()


class LoginForm(wtforms.Form):
    email = wtforms.StringField(
        validators=[Email(message='wrong email format')])
    password = wtforms.StringField(
        validators=[Length(min=3, max=20, message='wrong passsword format')])


class QuestionForm(wtforms.Form):
    title = wtforms.StringField(
        validators=[Length(min=3, max=20, message='wrong title format')])
    content = wtforms.StringField(
        validators=[Length(min=10, message='too little in content')])


class AnswerForm(wtforms.Form):
    content = wtforms.StringField(
        validators=[Length(min=3, message='too little in content')])
    question_id = wtforms.IntegerField(
        validators=[InputRequired(message='you need to input question id!')])
#
