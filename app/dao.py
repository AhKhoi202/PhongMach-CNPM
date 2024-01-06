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
    db.session.flush()
    return new_user


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


def get_examination_bill(medical_bill_id, examination_date):
    query = ExaminationBill.query
    if examination_date:
        query = query.filter(examination_date=examination_date)
    if medical_bill_id:
        return query.filter_by(medical_bill_id=medical_bill_id).first()
    return query.all()


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
    if regulation:
        return regulation.value
    return 0


def get_registration_form(examination_date):
    registration_forms = RegistrationForm.query.filter(
        RegistrationForm.examination_date == examination_date
    )
    return mappingFormsToData(registration_forms)


def delete_examination(examination_id):
    form = RegistrationForm.query.get(examination_id)
    if form:
        try:
            db.session.delete(form)
            db.session.commit()
            return True
        except:
            return False
    return False


def update_complete_form(complete_date):
    try:
        forms_to_update = RegistrationForm.query \
            .filter(RegistrationForm.examination_date == complete_date).all()
        if forms_to_update:
            for form in forms_to_update:
                form.accepted = True
            db.session.commit()
            return mappingFormsToData(forms_to_update)
        return []
    except:
        return []


def mappingFormsToData(forms):
    registration_data = []
    for form in forms:
        user = form.user
        registration_info = {
            "user_id": user.id,
            "fullname": user.fullname,
            "phone": user.phone,
            "birthday": user.birthday,
            "examination_date": form.examination_date,
            "id": form.id,
            "accepted": form.accepted
        }
        registration_data.append(registration_info)
    return registration_data


if __name__ == '__main__':
    with app.app_context():
        new_date = date(2024, 1, 3)
        bill = get_regulation_value('user_in_1_day')
        print(bill)
        registration_data = get_registration_form(new_date)
        print(registration_data)
