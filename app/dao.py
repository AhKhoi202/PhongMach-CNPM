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
        # user
        # register_user(username="admin",
        #               password="123456",
        #               fullname="Admin",
        #               gender=Gender.Male,
        #               phone="0386904554",
        #               role=Role.Admin)
        # for i in range(10):
        #     register_user(username=f'nguoikham{i}',
        #                   password="123456",
        #                   fullname=f'NguoiKham {i}',
        #                   gender=Gender.Female,
        #                   phone=f"09{i}{i}{i}{i}{i}{i}{i}{i}",
        #                   role=Role.Customer)
        # # Đơn vị thuốc
        # u1 = Unit(name="Chai")
        # u2 = Unit(name="Vĩ")
        # u3 = Unit(name="Viên")
        # db.session.add_all([u1, u2, u3])
        # db.session.commit()
        #
        # # Quy định
        # db.session.add_all([Regulation(regulation="Số bệnh nhân khám trong 1 ngày", value=40, user_id=1)])
        # db.session.commit()
        # medicine1 = Medicine(
        #     name="Thuốc 1",
        #     price=10.0,
        #     description="Mô tả cho Thuốc 1",
        #     direction="Hướng dẫn sử dụng cho Thuốc 1",
        #     unit_in_stock=100,
        #     unit_id=1 # Giả sử unit1.id là id của đơn vị Chai
        # )
        #
        # medicine2 = Medicine(
        #     name="Thuốc 2",
        #     price=15.0,
        #     description="Mô tả cho Thuốc 2",
        #     direction="Hướng dẫn sử dụng cho Thuốc 2",
        #     unit_in_stock=50,
        #     unit_id=2  # Giả sử unit2.id là id của đơn vị Vĩ
        # )
        #
        # # Thêm các đối tượng medicine vào phiên làm việc và commit vào cơ sở dữ liệu
        # db.session.add_all([medicine1, medicine2])
        # db.session.commit()
        # for i in range(12,22):
        #
        #     registration_form = RegistrationForm(user_id={i}, examination_date='2023-12-10')
        #     db.session.add(registration_form)
        db.session.commit()

