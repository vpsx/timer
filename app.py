# -*- coding: utf-8 -*-
"""
Мат-таймер)))00000

FORKED FROM:
---------------------------------
author: Grey Li
blog: withlihui.com
email: withlihui@gmail.com
github: github.com/greyli
column: zhuanlan.zhihu.com/flask
---------------------------------
A simple timer made with Flask and JavaScript.
https://github.com/helloflask/timer
---------------------------------
MIT license.
"""
import re
from flask import Flask, render_template, url_for, redirect, request, flash

app = Flask(__name__)
app.config['SECRET_KEY'] = 'А зачем я здесь?? Не понимаю(('


@app.route('/')
def index():
    return render_template('index.html', num=0)
