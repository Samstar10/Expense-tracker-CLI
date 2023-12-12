from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime
from sqlalchemy import declarative_base, relationship
from sqlalchemy_utils import PasswordType
from datetime import datetime

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password = Column(PasswordType(schemes=['bcrypt']), nullable=False)

class Category(Base):
    __tablename__ = 'categories'
    id = Column(Integer, primary_key = True)
    name = Column(String(50), unique=True, nullable=False)

class Expense(Base):
    __tablename__ = 'expenses'
    id = Column(Integer, primary_key=True)
    amount = Column(Integer, nullable=False)
    description = Column(String(255))
    date = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey('users.id'), nullable='False')
    category_id = Column(Integer, ForeignKey('categories.id'), nullable='False')


engine = create_engine('sqlite:///expense_tracker.db')
Base.metadata.create_all(engine)
