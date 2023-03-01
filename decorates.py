'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-26 13:15:31
LastEditors: alexthezhang228 zhangy32@tcd.ie
LastEditTime: 2023-02-26 23:33:23
FilePath: /flask_project/decorates.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''
from functools import wraps
from flask import g,redirect,url_for


def login_required(func):
    #保留func的信息
    @wraps(func)
    def inner(*args,**kwargs):
        if g.user:
            return func(*args,**kwargs)
        else:
            return redirect(url_for('author.login'))
    return inner

# @login_required
# def public_question(question_id):
#     pass
    