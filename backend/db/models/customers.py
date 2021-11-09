from sqlalchemy import Column,Integer,String
from db.base_class import Base

class Customer(Base):
    id = Column(Integer,primary_key=True,index=True)
    name = Column(String,nullable=False)
    lastname = Column(String,nullable=False)
    email = Column(String,nullable=False,unique=True,index=True)
    location = Column(String,nullable=False)