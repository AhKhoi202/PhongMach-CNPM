import cloudinary.uploader
from flask import render_template, request, redirect, url_for
from app import app, login_manager, dao
from app.models import Gender, Role


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
        form = request.form
        username = form.get('username')
        if dao.get_user_by_username(username):
            return render_template('auth/register.html', err_msg="Tên đăng nhập đã tồn tại")

        fullname = form.get('fullname')
        password = form.get('password')
        birthday = form.get('birthday')
        email = form.get('email')
        phone = form.get('phone')
        avatar_file = request.files.get('avatar_file')

        avatar = ''
        if avatar_file:
            res = cloudinary.uploader.upload(avatar_file)
            avatar = res['secure_url']

        try:
            dao.register_user(username=username,
                              password=password,
                              fullname=fullname,
                              gender=Gender.Male,
                              phone=phone,
                              role=Role.Customer,
                              email=email,
                              birthday=birthday,
                              avatar=avatar)
        except:
            err_msg = 'Đã có lỗi xảy ra! Vui lòng quay lại sau!'
        else:
            return redirect('/login')

    return render_template('auth/register.html')


@login_manager.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
