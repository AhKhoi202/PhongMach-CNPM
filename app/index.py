import math

from flask import render_template, request, redirect, session, jsonify
import dao
import utils
from app import app, login_manager
from flask_login import login_user

from app.models import User


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/about-us')
def about_us():
    return render_template('about/about_us.html')


@app.route('/services')
def services():
    return render_template('about/services.html')


@login_manager.user_loader
def load_user(user_id):
    return User(id=user_id)


if __name__ == '__main__':
    app.run(debug=True)
