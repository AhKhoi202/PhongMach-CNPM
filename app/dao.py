from app.models import User, Role, MedicalBill, MedicalBillDetail, ExaminationBill, Medicine, RegistrationForm, \
    MedicineTag, Regulation, Gender, Unit
from app import app, db
import hashlib


def get_user_by_id(user_id):
    return User.query.get(user_id)


def auth_user(username, password, role=Role.Customer):
    password = str(hashlib.md5(password.strip().encode('utf-8')).hexdigest())

    return User.query.filter(User.username.__eq__(username.strip()),
                             User.password.__eq__(password),
                             User.role.__eq__(role)).first()


def register_user(**kwargs):
    new_user = User(**kwargs)
    db.session.add(new_user)
    db.session.commit()


if __name__ == '__main__':
    with app.app_context():
        # # user
        register_user(username="admin", password="123456", fullname="Admin", gender=Gender.Male, phone="0386904554", role=Role.Admin)
        for i in range(10):
            register_user(username=f'nurseinnutshell{i}',
                          password="123456",
                          fullname=f'Nurse {i}',
                          gender=Gender.Female,
                          phone=f"09{i}{i}{i}{i}{i}{i}{i}{i}",
                          role=Role.Nurse)
        # Đơn vị thuốc
        u1 = Unit(name="Chai")
        u2 = Unit(name="Vĩ")
        u3 = Unit(name="Viên")
        db.session.add_all([u1, u2, u3])
        db.session.commit()

        # Quy định
        db.session.add_all([Regulation(regulation="Số bệnh nhân khám trong 1 ngày", value=40, user_id=1)])
        db.session.commit()
