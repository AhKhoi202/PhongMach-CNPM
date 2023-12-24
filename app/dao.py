from app.models import User, Role, MedicalBill, MedicalBillDetail, ExaminationBill, Medicine, RegistrationForm, \
    MedicineTag, Regulation, Gender, Unit
from app import app, db
import hashlib


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password)).first()


def register_user(**kwargs):
    new_user = User(**kwargs)
    db.session.add(new_user)
    db.session.commit()


def get_units():
    return Unit


def get_medicines():
    return Medicine.query


def update_user(user_id, **kwargs):
    user = get_user_by_id(user_id)
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.session.commit()


def registration_form(**kwargs):
    form = RegistrationForm(**kwargs)
    db.session.add(form)
    db.session.commit()
