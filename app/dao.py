from datetime import datetime, date

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


def update_user(user_id, **kwargs):
    user = get_user_by_id(user_id)
    for key, value in kwargs.items():
        setattr(user, key, value)
    db.session.commit()


def get_units():
    return Unit.query.all()


# name, description, direction
def get_medicines(**kwargs):
    query = Medicine.query
    for key, value in kwargs.items():
        if hasattr(Medicine, key):
            query = query.filter(getattr(Medicine, key).ilike(f"%{value}%"))

    medicines = query.all()
    return medicines


def get_medical_bill(patient_id=None, phone=None):
    query = MedicalBill.query
    if patient_id is not None:
        query = query.filter(MedicalBill.patient_id == patient_id)
    if phone is not None:
        query = query.join(User).filter(User.phone == phone)
    medical_bills = query.all()
    return medical_bills


def get_examination_bill(medical_bill_id):
    return ExaminationBill.query.filter_by(medical_bill_id=medical_bill_id).first()


def get_medical_bill_detail(medical_bill_id):
    return MedicalBillDetail.query.filter_by(medical_bill_id=medical_bill_id).all()


def count_registration_forms_by_date(examination_date=None):
    if examination_date is None:
        return 0
    start_of_day = datetime.combine(examination_date, datetime.min.time())
    end_of_day = datetime.combine(examination_date, datetime.max.time())
    return (
        RegistrationForm.query
        .filter(RegistrationForm.examination_date >= start_of_day, RegistrationForm.examination_date <= end_of_day)
        .count()
    )


def registration_form(**kwargs):
    form = RegistrationForm(**kwargs)
    db.session.add(form)
    db.session.commit()


def get_regulation_value(key):
    regulation = Regulation.query.filter_by(key=key).first()
    return regulation.value


if __name__ == '__main__':
    with app.app_context():
        new_date = date(2023, 12, 25)
        bill = get_regulation_value('user_in_1_day')
        print(bill)
