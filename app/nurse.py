from flask import redirect
from flask_admin import Admin, BaseView, expose, AdminIndexView
from flask_admin.contrib.sqla import ModelView
from app import app, db, admin
from app.models import Role, User, Medicine, RegistrationForm, Regulation
from flask_login import logout_user, current_user


class NurseIndexView(BaseView):
    def __init__(self, name=None, category=None,
                 endpoint=None, url=None,
                 template='admin/index.html',
                 menu_class_name=None,
                 menu_icon_type=None,
                 menu_icon_value=None):
        super(NurseIndexView, self).__init__(name or 'Home',
                                             category,
                                             endpoint or 'admin',
                                             '/admin' if url is None else url,
                                             'static',
                                             menu_class_name=menu_class_name,
                                             menu_icon_type=menu_icon_type,
                                             menu_icon_value=menu_icon_value)
        self._template = template

    @expose()
    def index(self):
        return self.render(self._template)



class MyNurseView(NurseIndexView):

    def __init__(self, name=None, **kwargs):
        super(MyNurseView, self).__init__(name=name, **kwargs)

    @expose('/')
    def index(self):
        return self.render('admin/nurses/index.html')


nurse = Admin(app=app,
              name="Y tá hệ thống Phòng mạch",
              template_mode='bootstrap4',
              url='/nurse',
              endpoint='nurse',
              index_view=MyNurseView(name="Trang chủ"))