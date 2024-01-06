from datetime import datetime, date

from flask import redirect, request
from flask_admin import Admin, BaseView, expose, AdminIndexView
from app import app, db, admin, dao, utils
from app.models import Role, User, Medicine, RegistrationForm, Regulation
from flask_login import logout_user, current_user


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == Role.Admin


class MyNurseView(AdminIndexView):

    def __init__(self, name=None, **kwargs):
        super(MyNurseView, self).__init__(name=name, **kwargs)

    @expose('/')
    def index(self):
        return self.render('admin/nurses/index.html')


class NurseRegisterView(AuthenticatedUser):
    @expose('/', methods=['GET', 'POST'])
    def nurse_register(self):
        template_str = 'admin/nurses/medical-appointment.html'
        if request.method == 'GET':
            return self.render(template_str)

        form = request.form
        examination_date = form.get('appointmentDate')
        examination_date = datetime.strptime(examination_date, '%Y-%m-%d').date()
        user_in_1_day = dao.get_regulation_value('user_in_1_day')
        if dao.count_registration_forms_by_date(examination_date) >= user_in_1_day:
            error_message = f"Đã đạt giới hạn {user_in_1_day} lần đăng ký " \
                            f"trong ngày {examination_date.strftime('%d-%m-%Y')}!!!"
            return self.render(template_str,
                               err_msg=error_message,
                               form_data=form)

        if utils.is_past_date(examination_date):
            error_message = "Ngày đăng ký phải là hôm nay hoặc tương lai!!!"
            return self.render('admin/nurses/medical-appointment.html',
                               err_msg=error_message,
                               form_data=form)

        fullname = form.get('fullname')
        birthday = form.get('birthday')
        phone = form.get('phone')
        email = form.get('email')
        gender = form.get('gioiTinh')

        if not fullname:
            error_message = "Chưa nhập họ tên bệnh nhân!!!"
            return self.render(template_str,
                               err_msg=error_message,
                               is_fullname_error=True,
                               form_data=form)
        if not birthday or not utils.is_past_date(birthday):
            error_message = "Ngày sinh phải là quá khứ!!!"
            return self.render(template_str,
                               err_msg=error_message,
                               is_birthday_error=True,
                               form_data=form)
        if not phone or len(phone) != 10:
            error_message = "Chưa nhập số điện thoại bệnh nhân hoặc số điện thoại không hợp lệ!!!"
            return self.render(template_str,
                               err_msg=error_message,
                               is_phone_error=True,
                               form_data=form)

        patient = dao.register_user(fullname=fullname,
                                    username=phone,
                                    birthday=birthday,
                                    phone=phone,
                                    gender=gender,
                                    email=email,
                                    password="123456"
                                    )
        dao.registration_form(user=patient,
                              examination_date=examination_date)
        return self.render(template_str, success_msg="Đăng ký lịch hẹn thành công!!!")


class NurseCompleteView(AuthenticatedUser):
    @expose('/', methods=['GET', 'POST'])
    def nurse_complete(self):
        today = datetime.today().date()
        examination_date = request.args.get('examination-date')
        if examination_date is None:
            examination_date = today
        else:
            examination_date = datetime.strptime(examination_date, "%Y-%m-%d").date()
        if request.method == 'GET':

            registration_data = dao.get_registration_form(examination_date)

            return self.render('admin/nurses/complete-view.html',
                               registration_data=registration_data,
                               examination_date=examination_date,
                               today=today)
        complete_date = request.form.get('complete-date')
        data = dao.update_complete_form(complete_date)
        # send SMS
        utils.send_SMS(utils.get_phones(data), complete_date)
        return self.render('admin/nurses/complete-view.html',
                           registration_data=data,
                           examination_date=examination_date,
                           today=today,
                           accepted=True)


class NurseCompletePayment(AuthenticatedUser):
    @expose('/', methods=['GET', 'POST'])
    def complete_payment(self):
        if request.method == 'GET':
            return self.render('admin/nurses/complete-payment.html')

        return self.render('admin/nurses/complete-payment.html')


class NurseLogoutView(AuthenticatedUser):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/')


nurse = Admin(app=app,
              name="Y tá hệ thống Phòng mạch",
              template_mode='bootstrap4',
              url='/nurse',
              endpoint='nurse',
              index_view=MyNurseView(name="Trang chủ", endpoint="nurse", url="/nurse"))
nurse.add_view(NurseRegisterView(name="Đăng ký khám", endpoint="register"))
nurse.add_view(NurseCompleteView(name="Hoàn tất lịch khám", endpoint="complete"))
nurse.add_view(NurseCompletePayment(name="Thanh toán hóa đơn", endpoint="payment"))
nurse.add_view(NurseLogoutView(name="Đăng xuất"))
