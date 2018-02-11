from flask import Flask, render_template
from verkefni2 import app
from verkefni2 import model
bokalisti=model.bokalisti
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html',bokalisti=bokalisti)

@app.route('/book/<bokin>')
def book(bokin=None):
    return render_template('baekur.html', book=model.urlCheck(bokalisti,bokin).check())