from flask import Flask, render_template
from verkefni2 import jon
from verkefni2 import model
bokalisti=model.bokalisti
book=model.book
@jon.route('/')
@jon.route('/index')
def index():
    return render_template('index.html',list=book(bokalisti).nafn())