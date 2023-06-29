from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Person(Base):
    __tablename__ = "people"
    ssn = Column("ssn", Integer, primary_key=True)
    firstname = Column("firstname", String(16))
    lastname = Column("lastname", String(16))
    gender = Column("gender", CHAR)
    age = Column("age", Integer)


    def __init__ (self, ssn, firstname, lastname, gender, age):
        self.ssn = ssn
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f"({self.ssn}) {self.firstname} {self.lastname} ({self.gender},{self.age})"
    



host='localhost'
user='demouser'
password='demo'
database='dataengineer'
port = '3306'

engine = create_engine('mysql+mysqlconnector://demouser:demo@localhost:3306/dataengineer')
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()


person = Person(123123, "Mike", "Smith", "M", 35)
session.add(person)
session.commit()

