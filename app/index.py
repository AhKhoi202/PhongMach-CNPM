from datetime import datetime
import cloudinary.uploader
from cloudinary.provisioning import user
from flask import render_template, request, redirect, url_for
from flask_login import logout_user, login_user, current_user

from app import app, login_manager, dao, decorators
from app.models import Gender, Role
from app.utils import is_past_date


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
@decorators.anonymous_user
def login_process():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = dao.auth_user(username=username, password=password)
        if user:
            login_user(user=user)
            url_next = request.args.get('next')
            return redirect(url_next if url_next else '/')
        return redirect(url_for('index'))
    return render_template('auth/login.html')


@app.route('/register', methods=['GET', 'POST'])
@decorators.anonymous_user
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


@app.route('/logout')
@decorators.authenticated_user
def logout():
    logout_user()
    return redirect('/login')


@app.route('/registration-form', methods=['GET', 'POST'])
@decorators.authenticated_user
def registration_form_process():
    if request.method == 'GET':
        return render_template('registration-form.html')

    form = request.form
    examination_date = request.form.get('examination_date')
    examination_date = datetime.strptime(examination_date, '%Y-%m-%d').date()
    user_in_1_day = dao.get_regulation_value('user_in_1_day')
    if dao.count_registration_forms_by_date(examination_date) >= user_in_1_day:
        error_message = f"Đã đạt giới hạn {user_in_1_day} lần đăng ký " \
                        f"trong ngày {examination_date.strftime('%d-%m-%Y')}!!!"
        return render_template('registration-form.html', err_msg=error_message)

    if is_past_date(examination_date):
        error_message = "Ngày đăng ký phải là hôm nay hoặc tương lai!!!"
        return render_template('registration-form.html', err_msg=error_message)

    fullname = form.get('fullname')
    birthday = form.get('birthday')
    phone = form.get('phone')
    user_id = current_user.id
    dao.update_user(user_id=user_id,
                    fullname=fullname,
                    birthday=birthday,
                    phone=phone)
    dao.registration_form(user=current_user,
                          examination_date=examination_date)
    return render_template('registration-form.html', success_msg="Đăng ký lịch hẹn thành công!!!")


@app.route('/history')
@decorators.authenticated_user
def history():
    return render_template('examination-history.html')


@login_manager.user_loader
def load_user(user_id):
    return dao.get_user_by_id(user_id)


if __name__ == '__main__':
    app.run(debug=True)
