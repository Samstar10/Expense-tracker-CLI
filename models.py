from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import declarative_base, relationship
from sqlalchemy_utils import PasswordType
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    name = Column(String(50))

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer)
    description = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)
