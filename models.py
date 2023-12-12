from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy import declarative_base, relationship
from sqlalchemy_utils import PasswordType

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50))
    password = Column(String)