'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-19 11:18:16
LastEditors: alexthezhang228 110424337+alexthezhang228@users.noreply.github.com
LastEditTime: 2023-03-10 21:10:38
FilePath: /flask_project/app.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from flask import Flask, render_template, g, session
import config
from models import UserModel
from exts import db, mail
from blueprints.author import bp as bp_author
from blueprints.questions import bp as bp_question
from flask_migrate import Migrate


app = Flask(__name__, template_folder='template')
app.config.from_object(config)


db.init_app(app)
mail.init_app(app)
migrate = Migrate(app, db)


app.register_blueprint(bp_author)
app.register_blueprint(bp_question)

# //登陆前存储用户id，登录的时候可以直接使用


@app.before_request
def my_before_request():
    user_id = session.get('user_id')
    if user_id:
        user = db.session.get(UserModel, user_id)
        setattr(g, 'user', user)
    else:
        setattr(g, 'user', None)


@app.context_processor
def my_context_processor():
    return {'user': g.user}


if __name__ == '__main__':
    app.run(debug=True)
