import datetime
from sqlalchemy import create_engine, Column, Integer, String, Date, Float, ForeignKey, select, and_
from sqlalchemy.orm import relationship, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
engine = create_engine('postgresql://postgres:1@127.0.0.1:5432/Database1')
Session = sessionmaker(bind=engine)

def recreate_database():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)

class Apartment(Base):
    __tablename__ = 'Apartment'
    id_apartment = Column(Integer, primary_key=True)
    floor = Column(Integer)
    number = Column(Integer)
    number_of_rooms = Column(Integer)
    id_person = Column(Integer, ForeignKey('Person.id_person'))
    id_building = Column(Integer, ForeignKey('Building.id_building'))

    def __init__(self, id_apartment, floor, number, number_of_rooms, id_person, id_building):
        self.id_apartment = id_apartment
        self.floor = floor
        self.number = number
        self.number_of_rooms = number_of_rooms
        self.id_person = id_person
        self.id_building = id_building

    def __repr__(self):
        return "{} {} {} {} {} {}".format(self.id_apartment, self.floor, self.number, self.number_of_rooms, self.id_person, self.id_building)

class Building(Base):
    __tablename__ = 'Building'
    id_building = Column(Integer, primary_key=True)
    adress = Column(String)
    number_of_apartments = Column(Integer)
    number_of_floors = Column(Integer)
    Company_name = Column(String, ForeignKey('Company.Company_name'))

    def __init__(self, id_building, adress, number_of_apartments, number_of_floors, Company_name):
        self.id_building = id_building
        self.adress = adress
        self.number_of_apartments = number_of_apartments
        self.number_of_floors = number_of_floors
        self.Company_name = Company_name

    def __repr__(self):
        return "{} {} {} {} {}".format(self.id_building, self.adress, self.number_of_apartments, self.number_of_floors, self.Company_name)

class Company(Base):
    __tablename__ = 'Company'
    Company_name = Column(String, primary_key=True)
    adress = Column(String)
    phone = Column(String)

    def __init__(self, Company_name, adress, phone):
        self.Company_name = Company_name
        self.adress = adress
        self.phone = phone

    def __repr__(self):
        return "{} {} {}".format(self.Company_name, self.adress, self.phone)

class Person(Base):
    __tablename__ = 'Person'
    id_person = Column(Integer, primary_key=True)
    name = Column(String)
    surname = Column(String)
    patronymic = Column(String)
    phone = Column(String)
    Company_name = Column(String, ForeignKey('Company.Company_name'))

    def __init__(self, id_person, name, surname, patronymic, phone, Company_name):
        self.id_person = id_person
        self.name = name
        self.surname = surname
        self.patronymic = patronymic
        self.phone = phone
        self.Company_name = Company_name

    def __repr__(self):
        return "{} {} {} {} {} {}".format(self.id_person, self.name, self.surname, self.patronymic, self.phone, self.Company_name)

class Model:
    def __init__(self):
        self.session = Session()
        self.connection = engine.connect()

    def print_Apartment(self):
        return self.session.query(Apartment).order_by(Apartment.id_apartment.asc()).all()

    def print_Building(self):
        return self.session.query(Building).order_by(Building.id_building.asc()).all()

    def print_Company(self):
        return self.session.query(Company).order_by(Company.Company_name.asc()).all()

    def print_Person(self):
        return self.session.query(Person).order_by(Person.id_person.asc()).all()

    def insert_Apartment(self, id_apartment: int, floor: int, number: int, number_of_rooms: int, id_person: int, id_building: int) -> None:
        New_Apartment = Apartment(id_apartment, floor, number, number_of_rooms, id_person, id_building)
        self.session.add(New_Apartment)
        self.session.commit()

    def insert_Building(self, id_building: int, adress: str, number_of_apartments: int, number_of_floors: int, Company_name: str) -> None:
        New_Building = Building(id_building, adress, number_of_apartments, number_of_floors, Company_name)
        self.session.add(New_Building)
        self.session.commit()

    def insert_Company(self, Company_name: str, adress: str, phone: str) -> None:
        New_Company = Company(Company_name, adress, phone)
        self.session.add(New_Company)
        self.session.commit()

    def insert_Person(self, id_person: int, name: str, surname: str, patronymic: str, phone: str, Company_name: str) -> None:
        New_Person = Person(id_person, name, surname, patronymic, phone, Company_name)
        self.session.add(New_Person)
        self.session.commit()

    def delete_Apartment(self, id_apartment) -> None:
        self.session.query(Apartment).filter_by(id_apartment=id_apartment).delete()
        self.session.commit()

    def delete_Building(self, id_building) -> None:
        self.session.query(Building).filter_by(id_building=id_building).delete()
        self.session.commit()

    def delete_Company(self, Company_name) -> None:
        self.session.query(Company).filter_by(Company_name=Company_name).delete()
        self.session.commit()

    def delete_Person(self, id_person) -> None:
        self.session.query(Person).filter_by(id_person=id_person).delete()
        self.session.commit()

    def update_Apartment(self, id_apartment: int, floor: int, number: int, number_of_rooms: int, id_person: int, id_building: int) -> None:
        self.session.query(Apartment).filter_by(id_apartment=id_apartment).update({Apartment.floor: floor, Apartment.number: number, Apartment.number_of_rooms: number_of_rooms, Apartment.id_person: id_person, Apartment.id_building: id_building})
        self.session.commit()

    def update_Building(self, id_building: int, adress: str, number_of_apartments: int, number_of_floors: int, Company_name: str) -> None:
        self.session.query(Building).filter_by(id_building=id_building).update({Building.adress: adress, Building.number_of_apartments: number_of_apartments, Building.number_of_floors: number_of_floors, Building.Company_name: Company_name})
        self.session.commit()

    def update_Company(self, Company_name: str, adress: str, phone: str) -> None:
        self.session.query(Company).filter_by(Company_name=Company_name).update({Company.adress: adress, Company.phone: phone})
        self.session.commit()

    def update_Person(self, id_person: int, name: str, surname: str, patronymic: str, phone: str, Company_name: str) -> None:
        self.session.query(Person).filter_by(id_person=id_person).update({Person.name: name, Person.surname: surname, Person.patronymic: patronymic, Person.phone: phone, Person.Company_name: Company_name})
        self.session.commit()

    def find_pk_Apartment(self, value: int):
        return self.session.query(Apartment).filter_by(id_apartment=value).first()
    
    def find_pk_Building(self, value: int):
        return self.session.query(Building).filter_by(id_building=value).first()

    def find_pk_Company(self, value: str):
        return self.session.query(Company).filter_by(Company_name=value).first()

    def find_pk_Person(self, value: int):
        return self.session.query(Person).filter_by(id_person=value).first()

    def find_fk_Apartment(self, value: int, table_name: str):
        if table_name == "Building":
            return self.session.query(Apartment).filter_by(id_building=value).first()
        elif table_name == "Person":
            return self.session.query(Apartment).filter_by(id_person=value).first()

    def find_fk_Building(self, value: str):
        return self.session.query(Building).filter_by(Company_name=value).first()

    def find_fk_Person(self, value: str):
        return self.session.query(Person).filter_by(Company_name=value).first()