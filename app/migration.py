from app.models import User, Role, MedicalBill, MedicalBillDetail, ExaminationBill, Medicine, RegistrationForm, \
    MedicineTag, Regulation, Gender, Unit
from app import app, dao, db
import hashlib

if __name__ == '__main__':
    with app.app_context():
        # user
        dao.register_user(username="admin",
                          password="123456",
                          fullname="Admin",
                          gender=Gender.Male,
                          phone="0386904554",
                          role=Role.Admin)
        for i in range(10):
            dao.register_user(username=f'nguoikham{i}',
                              password="123456",
                              fullname=f'NguoiKham {i}',
                              gender=Gender.Female,
                              phone=f"09{i}{i}{i}{i}{i}{i}{i}{i}",
                              role=Role.Customer)
        # Đơn vị thuốc
        u1 = Unit(name="Chai")
        u2 = Unit(name="Vĩ")
        u3 = Unit(name="Viên")
        u4 = Unit(name="Gói")
        db.session.add_all([u1, u2, u3, u4])
        db.session.commit()

        # Quy định
        db.session.add_all([Regulation(key="user_in_1_day", description="Số bệnh nhân khám trong 1 ngày", value=40, user_id=1)])
        db.session.commit()

        db.session.commit()

        m1 = Medicine(
            name="A.T Alugela",
            price=1500,
            description="Viêm thực quản, viêm dạ dày cấp và mạn tính, viêm loét dạ dày tá tràng, kích ứng dạ dày, ợ chua, rát bỏng",
            direction="1-2 gói thuốc, từ 2-3 lần mỗi ngày, uống trước ăn 30 phút.",
            unit_in_stock=100,
            unit_id=4,
        )

        m2 = Medicine(
            name="A.T Bisoprolol 5",
            price=500,
            description="điều trị tăng huyết áp, đau thắt ngực ổn định mạn tính, suy tim mạn tính",
            direction="Uống thuốc với nhiều nước, nên dùng thuốc vào buổi sáng khi đói hoặc lúc điểm tâm. Không được nhai.",
            unit_in_stock=100,
            unit_id=3,
        )

        m3 = Medicine(
            name="A.T Furosemid inj",
            price=750,
            description="điều trị phù, tăng huyết áp thể nhẹ và trung bình",
            direction="uống ngay sau khi ăn bữa ăn chính.",
            unit_in_stock=100,
            unit_id=1,
        )
        m4 = Medicine(
            name="A.T Hydrocortisone",
            price=5000,
            description="sử dụng điều trị chống viêm như viêm khớp, lupus, bệnh gout, viêm khớp vảy nến, viêm loét ruột.",
            direction="Dùng thuốc đường tiêm khi người bệnh không thể tiếp nhận thuốc bằng đường khác.",
            unit_in_stock=100,
            unit_id=1,
        )
        m5 = Medicine(
            name="A.T Nitroglycerin inj",
            price=50000,
            description="Suy tim, nhồi máu cơ tim cấp, phù phổi cấp do tim, đau thắt ngực trầm trọng.",
            direction="i pha loãng trong dextrose 5% hoặc natri clorid 0,9% trước khi truyền tinh mach.",
            unit_in_stock=100,
            unit_id=1,
        )
        m6 = Medicine(
            name="A.T Sucralfate",
            price=1100,
            description="điều trị viêm loét dạ dày tá tràng.",
            direction="1g/lần, 4 lần/ngày (uống 1 giờ trước 3 bữa ăn và trước khi đi ngủ)",
            unit_in_stock=100,
            unit_id=4,
        )
        m7 = Medicine(
            name="Acecyst ",
            price=200,
            description="Acecyst thuốc có tác dụng long đờm, được sử dụng để làm thông đường hô hấp",
            direction="Sử dụng liều 1 viên/ lần, ngày 3 lần.",
            unit_in_stock=100,
            unit_id=3,
        )
        m8 = Medicine(
            name="Acefalgan",
            price=550,
            description="giảm đau và hạ sốt, có tác dụng giảm đau từ nhẹ đến trung bình và hạ sốt.",
            direction="Uống một viên mỗi 4 đến 6 giờ, nếu bạn cần. Không uống nhiều hơn 4 viên trong bất kỳ 24 giờ nào.",
            unit_in_stock=100,
            unit_id=3,
        )
        m9 = Medicine(
            name="Adrenalin",
            price=2500,
            description="ác dụng kích thích hệ thần kinh giao cảm, kích thích cả thụ thể alpha và thụ thể beta của thần kinh giao cảm",
            direction="Tiêm dưới da hoặc tiêm bắp từ 0,3-0,5 ml dung dịch tỷ lệ 1:1000, nhắc lại 5 phút một lần tùy theo huyết áp của bệnh nhân.",
            unit_in_stock=100,
            unit_id=1,
        )
        m10 = Medicine(
            name="Agifuros",
            price=90,
            description="làm tăng thải trừ các ion kéo theo nước, tăng lưu lượng máu, tăng độ lọc ở cầu thận",
            direction="Thuốc Agifuros 40mg được dùng đường uống. Nên uống trọn viên thuốc với một ly nước đầy.",
            unit_in_stock=100,
            unit_id=2,
        )
        m11 = Medicine(
            name="Bepracid 20",
            price=500,
            description="có tác dụng ức chế tiết acid dạ dày trong điều kiện bình thường và trong cả tình trạng kích thích ",
            direction="20 mg/ lần/ ngày trong 4 – 8 tuần.",
            unit_in_stock=100,
            unit_id=2,
        )
        m12 = Medicine(
            name="Bicebid 200",
            price=1000,
            description="sử dụng trong việc điều trị các bệnh nhiễm khuẩn như: nhiễm khuẩn đường tiết niệu và nhiễm khuẩn đường hô hấp trên - dưới",
            direction="dùng liều 300mg/ngày",
            unit_in_stock=100,
            unit_id=2,
        )
        m13 = Medicine(
            name="Bifucil",
            price=600,
            description="Bifucil thuộc nhóm thuốc trị ký sinh trùng, chống nhiễm khuẩn, kháng virus và kháng nấm.",
            direction="Uống 1 viên/ lần, 1 – 2 lần/ngày. Dùng trong 7 - 14 ngày.",
            unit_in_stock=100,
            unit_id=2,
        )
        m14 = Medicine(
            name="Captagim",
            price=76,
            description="Captagim thuộc nhóm thuốc tim mạch, được bào chế dưới dạng viên nén",
            direction="25mg x 2 - 3 lần/ ngày. Trường hợp bệnh nặng có thể tăng liều Captagim đến 50mg x 3 lần/ ngày;",
            unit_in_stock=100,
            unit_id=3,
        )
        m15 = Medicine(
            name="Cerecaps",
            price=3000,
            description="thuốc điều trị thiếu máu não là một thuốc có nguồn gốc dược liệu, được điều chế ở dạng viên nang cứng",
            direction="uống 2-3 viên mỗi lần, ngày dùng 2 lần.",
            unit_in_stock=100,
            unit_id=2,
        )
        m16 = Medicine(
            name="Ciloxan",
            price=69000,
            description="Thuốc Ciloxan có dạng bào chế là dung dịch nhỏ mắt.",
            direction="Trong 6 giờ đầu nhỏ 2 giọt sau mỗi 15 phút, 4 giờ sau thì 2 giọt sau mỗi 30 phút.",
            unit_in_stock=100,
            unit_id=1,
        )
        m17 = Medicine(
            name="Clanzen",
            price=200,
            description="thuốc chống dị ứng",
            direction=" 5mg/ngày, 2 ngày dùng 1 lần.",
            unit_in_stock=100,
            unit_id=3,
        )
        m18 = Medicine(
            name="Comegim",
            price=365,
            description="thành phần chính là perindopril erbumin, là thuốc điều trị tăng huyết áp.",
            direction="Thuốc thường được cho uống một lần/ngày vào buổi sáng, lúc đói (trước bữa ăn).",
            unit_in_stock=100,
            unit_id=3,
        )
        m19 = Medicine(
            name="Daflon",
            price=3258,
            description="Thuốc có tác dụng làm giảm sức căng và tình trạng ứ trệ của tĩnh mạch, bảo vệ, làm tăng bền của các mạch máu nhỏ.",
            direction="uống 1 viên x2 lần/ngày vào các bữa ăn.",
            unit_in_stock=100,
            unit_id=3,
        )
        m20 = Medicine(
            name="Desloratadin",
            price=160,
            description="giúp người bệnh nâng cao hiệu quả điều trị và tránh được những tác dụng phụ không mong muốn.",
            direction="liều khuyến cáo là 5 mg, 2 ngày uống 1 lần (uống cách ngày).",
            unit_in_stock=100,
            unit_id=3,
        )
        m21 = Medicine(
            name="Dextrose",
            price=13000,
            description="bổ sung glucose cho những đối tượng dễ bị hạ đường huyết như suy dinh dưỡng",
            direction="sử dụng từ 10- 25g, có thể lặp lại trong trường hợp nghiêm trọng;",
            unit_in_stock=100,
            unit_id=1,
        )
        m22 = Medicine(
            name="Dimedrol",
            price=650,
            description="tác dụng kháng histamin, an thần, chống nôn và chống co thắt",
            direction="Tiêm bắp hoặc tĩnh mạch, 10 – 50mg/lần.",
            unit_in_stock=100,
            unit_id=1,
        )
        m23 = Medicine(
            name="Entacron 25",
            price=1500,
            description="thuốc được sử dụng trong các bệnh lý như bệnh thận, bệnh gan, bệnh tim gây ra phù, cổ chướng và cũng được dùng phối hợp trong bệnh tăng huyết áp.",
            direction="Liều ban đầu uống 50- 100 mg/ngày, chia từ 2 đến 4 lần, dùng ít nhất 2 tuần",
            unit_in_stock=100,
            unit_id=3,
        )
        m24 = Medicine(
            name="Erolin",
            price=2500,
            description="Thuốc được sử dụng trong điều trị dị ứng, mày đay,... ",
            direction="Dùng liều 10mg/ngày, tương đương 1 viên thuốc Erolin 10mg/ngày;",
            unit_in_stock=100,
            unit_id=2,
        )
        m25 = Medicine(
            name="Expas 40",
            price=760,
            description="một loại thuốc chống co thắt được sử dụng để thư giãn các cơ trơn như của đường tiêu hóa",
            direction="Uống 1-2 viên một lần uống 3 lần/ngày.",
            unit_in_stock=100,
            unit_id=2,
        )
        m26 = Medicine(
            name="Fefasdin",
            price=10500,
            description="thuốc chống dị ứng (thuộc nhóm thuốc kháng Histamin thế hệ 2) thường dùng trong các trường hợp quá mẫn cảm, dị ứng theo mùa, ...",
            direction="Uống 60mg/lần, ngày chia 2 lần. Nếu dùng Fefasdin 120 hay 180 thì uống 1 viên trong ngày;",
            unit_in_stock=100,
            unit_id=1,
        )
        m27 = Medicine(
            name="Fenilham",
            price=11500,
            description="thuốc giảm đau thuộc nhóm opioid, thường được chỉ định giảm đau trong ung thư, phẫu thuật gây mê và giảm đau sau phẫu thuật.",
            direction=" 50 – 100 microgam/ lần. Tiêm tĩnh mạch tốc độ chậm.",
            unit_in_stock=100,
            unit_id=1,
        )
        m28 = Medicine(
            name="Galanmer",
            price=400,
            description="huộc nhóm vitamin và khoáng chất, thuốc Galanmer có tác dụng điều trị và phòng ngừa thiếu vitamin B12",
            direction="1 lần/ viên và uống 3 lần/ ngày.",
            unit_in_stock=100,
            unit_id=2,
        )
        m29 = Medicine(
            name="Gyoryg",
            price=600,
            description="người tăng glucose máu (đặc biệt tăng glucose máu sau khi ăn) không kiểm soát được chỉ bằng chế độ ăn và tập luyện.",
            direction="Uống acarbose vào đầu bữa ăn để giảm nồng độ glucose máu sau ăn",
            unit_in_stock=100,
            unit_id=3,
        )
        m30 = Medicine(
            name="Hapacol",
            price=1500,
            description="Hapacol được sử dụng phổ biến trong điều trị các triệu chứng thường gặp như sốt cao, đau đầu, mệt mỏi,…",
            direction="1 viên/lần, nếu người bệnh bị đau nhức nghiêm trọng có thể dùng 2 viên/lần hoặc sử dụng theo chỉ định của bác sĩ.",
            unit_in_stock=100,
            unit_id=4,
        )
        db.session.add_all([m1, m2, m3, m4, m5, m6, m7, m8, m9, m10, m11, m12, m13, m14, m15, m16, m17, m18, m19, m20,
                            m21, m22, m23, m24, m25, m26, m27, m28, m29, m30])
        db.session.commit()
