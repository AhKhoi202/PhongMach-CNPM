from flask import Flask, Blueprint
from urllib.parse import quote

from flask_admin import Admin, AdminIndexView, expose
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
# from flask_babelex import Babel
import cloudinary

app = Flask(__name__)
# app
app.secret_key = 'zaq12wsxcde34rfvbgt56yhnmju78ik,.lo90p;/'
login_manager = LoginManager(app=app)
# babel = Babel(app=app)
# @babel.localeselector
# def load_locale():
#     return 'vi'
# database config
# app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:%s@localhost:3306/phongmachdb?charset=utf8mb4' % quote('')
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ahkhoi202:%s@ahkhoi202.mysql.pythonanywhere-services.com/ahkhoi202$default?charset=utf8mb4' % quote('Admin@123')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app=app)

# cloudinary (upload anh avatar)
cloudinary.config(cloud_name='dcvdmnrvo', api_key='483432986537474', api_secret='QuLYz0193idvCinKaxTNbh1u4io')

# twilio (gui sms)
from twilio.rest import Client

account_sid = 'AC28f8609c24a6201bb1fa843e4f5eb432'
auth_token = '5a50a4f5464face7b8ec8009284fb133'
client = Client(account_sid, auth_token)

# validation_request = client.validation_requests.create(
#                                 friendly_name='My Home Phone Number',
#                                 phone_number='+84387-73500'
#                             )
#
# print(validation_request.friendly_name)
# message = client.messages.create(
#   from_='+12013796798',
#   body='Hello test',
#   to='+84386904554'
# )

from app import admin
from app import nurse
