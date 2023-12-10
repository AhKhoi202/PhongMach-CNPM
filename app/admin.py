from flask import redirect
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Role, User
from flask_login import logout_user, current_user


admin = Admin(app=app, name='Quản trị hệ thống Phòng mạch', template_mode='bootstrap4')


class AuthenticatedAdmin(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated and current_user.user_role == Role.ADMIN


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AlwaysAccessView(BaseView):
    def is_accessible(self):
        return True


class UserView(AuthenticatedAdmin):
    column_list = ['name', 'products']


class MyStatsView(AlwaysAccessView):
    @expose("/")
    def index(self):
        return self.render('admin/pages/stats.html')


class MyLogoutView(AlwaysAccessView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/')


admin.add_view(UserView(User, db.session))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
admin.add_view(MyLogoutView(name='Đăng xuất'))