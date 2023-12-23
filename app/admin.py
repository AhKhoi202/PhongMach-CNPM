from flask import redirect
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app import app, db
from app.models import Role, User, Medicine, RegistrationForm, Regulation
from flask_login import logout_user, current_user


class AuthenticatedAdmin(ModelView):
    page_size = 8

    def is_accessible(self):
        return current_user.is_authenticated and current_user.role == Role.Admin


class AuthenticatedUser(BaseView):
    def is_accessible(self):
        return current_user.is_authenticated


class AlwaysAccessView(BaseView):
    def is_accessible(self):
        return True


class UserView(AuthenticatedAdmin):
    column_list = ['username', 'fullname', 'birthday', 'phone']
    column_labels = {
        'fullname': 'Họ tên',
        'birthday': 'Ngày sinh',
        'phone': 'Số điện thoại',
    }


class MedicineView(AuthenticatedAdmin):
    column_list = ['name', 'price', 'description', 'direction', 'unit_in_stock', 'unit.name']
    column_labels = {
        'name': 'Tên thuốc',
        'price': 'Giá',
        'description': 'Mô tả',
        'direction': 'Hướng dẫn sử dụng',
        'unit.name': 'Đơn vị',
        'unit_in_stock': 'Tồn kho',
    }
    column_filters = ('name', 'description')
    column_searchable_list = ('name', 'description', 'direction')
    column_exclude_list = ['medical_bill_details']


class RegistrationFormView(AuthenticatedAdmin):
    column_list = ['user.fullname', 'user.phone', 'examination_date', 'user.gender']
    column_labels = {
        'user.fullname': 'Tên bệnh nhân',
        'user.phone': 'Số điện thoại',
        'user.gender': 'Giới tính',
        'examination_date': 'Lịch khám',
    }
    can_create = False
    can_edit = False


class RegulationView(AuthenticatedAdmin):
    column_list = ['regulation', 'value']


class MyStatsView(AlwaysAccessView):
    @expose("/")
    def index(self):
        return self.render('admin/pages/stats.html')


class MyLogoutView(AlwaysAccessView):
    @expose("/")
    def index(self):
        logout_user()
        return redirect('/')


class MyAdminView(AdminIndexView):
    @expose('/')
    def index(self):
        return self.render('admin/pages/index.html')


admin = Admin(app=app,
              name='Quản trị hệ thống Phòng mạch',
              template_mode='bootstrap4',
              index_view=MyAdminView(name="Trang chủ"),
              endpoint='admin',
              url='/admin')
admin.add_view(UserView(User, db.session, name="Người dùng"))
admin.add_view(MedicineView(Medicine, db.session, name="Thuốc"))
admin.add_view(RegistrationFormView(RegistrationForm, db.session, name="Đơn đăng ký khám bệnh"))
admin.add_view(RegulationView(Regulation, db.session, name="Quy định"))
admin.add_view(MyStatsView(name='Thống kê báo cáo'))
admin.add_view(MyLogoutView(name='Đăng xuất'))
