from sqlalchemy.orm import relationship, backref
from app import db, app
from sqlalchemy import Column, Integer, String, Float, Enum, DateTime, Boolean, ForeignKey, Text, Date
from datetime import datetime, date
from flask_login import UserMixin
from enum import Enum as ModelEnum


class BaseModel(db.Model):
    __abstract__ = True
    id = Column(Integer, primary_key=True, autoincrement=True)


class Gender(ModelEnum):
    Male = 1
    Female = 2


class Role(ModelEnum):
    Admin = 1
    Customer = 2
    Nurse = 3
    Doctor = 4


class User(BaseModel, UserMixin):
    __tablename__ = 'user'
    fullname = Column(String(255), nullable=False)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(255), nullable=False)
    avatar = Column(String(255), nullable=True)
    gender = Column(String(20), default=Gender.Male)
    birthday = Column(Date)
    email = Column(String(255), nullable=True)
    phone = Column(String(11), nullable=True)
    active = Column(Boolean, default=True)
    created_date = Column(DateTime, default=datetime.now())
    role = Column(Enum(Role), default=Role.Customer)

    # details = relationship('ListDetail', backref='user', lazy=True)
    # bills = relationship('Bills', backref='user', lazy=True)

    def __str__(self):
        return self.fullname


class Unit(BaseModel):
    __tablename__ = 'unit'
    name = Column(String(50), nullable=False)
    medicines = relationship('Medicine', backref='unit_id', lazy=True)

    def __str__(self):
        return self.name


class Tag(BaseModel):
    __tablename__ = 'tag'
    name = Column(String(255), nullable=False)

    medicine_tags = relationship('MedicineTag', backref='tag_id', lazy=False)

    def __str__(self):
        return self.name


class Medicine(BaseModel):
    __tablename__ = 'medicine'
    name = Column(String(255), nullable=False)
    price = Column(Float, default=0)
    description = Column(Text, nullable=True)
    unit_in_stock = Column(Integer, default=0)
    unit_id = Column(Integer, ForeignKey(Unit.id), nullable=False)

    medicine_tags = relationship('MedicineTag', backref='medicine_id', lazy=False)

    def __str__(self):
        return self.name


class MedicineTag(BaseModel):
    __tablename__ = 'medicine_tag'
    tag_id = Column(Integer, ForeignKey(Tag.id), nullable=False)
    medicine_id = Column(Integer, ForeignKey(Medicine.id), nullable=False)

    def __str__(self):
        return self.medicine.name + self.tag.name


class Schedule(BaseModel):
    __tablename__ = ''


if __name__ == '__main__':
    with app.app_context():
        pass
        # db.create_all()
        # user1 = User(fullname='admin', username='admin', password='202cb962ac59075b964b07152d234b70',
        #              avatar='https://res.cloudinary.com/dxajszqyt/image/upload/v1670597632/ae382fmw4ye8lamhsvlc.png',
        #              role=Role.Admin)
        # db.session.add(user1)
        # db.session.commit()