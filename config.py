'''
Author: alexthezhang228 zhangy32@tcd.ie
Date: 2023-02-19 11:19:54
LastEditors: alexthezhang228 zhangy32@tcd.ie
LastEditTime: 2023-02-25 14:21:19
FilePath: /flask_project/config.py
Description: 这是默认设置,请设置`customMade`, 打开koroFileHeader查看配置 进行设置: https://github.com/OBKoro1/koro1FileHeader/wiki/%E9%85%8D%E7%BD%AE
'''

SECRET_KEY = 'ASDFGHJKL'

HOSTNAME = '127.0.0.1'
PORT = 3306
DATABASE = 'qa_project'
USERNAME = 'root'
PASSWORD = ''
DB_URI = 'mysql+pymysql://{}:{}@{}:3306/{}?charset=utf8'.format(
    USERNAME, PASSWORD, HOSTNAME,  DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI


MAIL_SERVER = 'smtp.gmail.com'
MAIL_USE_SSL = True
MAIL_USE_TLS = False
MAIL_PORT = 465
MAIL_USERNAME = 'zhangy32@tcd.ie'
MAIL_PASSWORD = '272829ASDzxc!'
MAIL_DEFAULT_SENDER = 'zhangy32@tcd.ie'
