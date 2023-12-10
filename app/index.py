from flask import render_template, request, redirect, url_for

from app import app, login_manager
from app.models import User


@app.route('/')
def index():
    return render_template('about/index.html')


@app.route('/about-us')
def about_us():
    return render_template('about/about_us.html')


@app.route('/services')
def services():
    return render_template('about/services.html')


@app.route('/news')
def news():
    return render_template('about/news.html')


@app.route('/contact')
def contact():
    return render_template('about/contact_us.html')


@app.route('/login', methods=['GET', 'POST'])
def login_process():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        return redirect(url_for('index'))
    return render_template('auth/login.html')


@app.route('/register', methods=['GET', 'POST'])
def register_process():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

    return render_template('auth/register.html')


@login_manager.user_loader
def load_user(user_id):
    return User.query.filter_by(id=user_id).first()


if __name__ == '__main__':
    app.run(debug=True)
