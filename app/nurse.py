from flask import redirect
from flask_admin import Admin, BaseView, expose, AdminIndexView
from app import app, db, admin
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

    @expose('/register', methods=['GET', 'POST'])
    def nurse_register(self):
        return self.render('admin/nurses/medical-appointment.html')

    def get_admin_menu(self):
        menu = super(MyNurseView, self).get_admin_menu()
        print("Menu Items:", menu)
        return super(MyNurseView, self).get_admin_menu() + [
            {'name': 'Register', 'url': self.get_url('nurse_register')}
        ]


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
nurse.add_view(NurseLogoutView(name="Đăng xuất"))
