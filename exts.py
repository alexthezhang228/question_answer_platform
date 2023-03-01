'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-19 11:59:40
LastEditors: alexthezhang228 zhangy32@tcd.ie
LastEditTime: 2023-02-20 20:26:06
FilePath: /flask_project/exts.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''


# 解决循环引用的问题
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
db=SQLAlchemy()
mail=Mail()