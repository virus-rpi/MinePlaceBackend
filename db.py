from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine('postgresql://your_username:your_password@your_host/your_database_name')

Base = declarative_base()


class Shop(Base):
    __tablename__ = 'shops'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    owner = Column(String)
    location = Column(String)
    rating = Column(Integer)
    items = Column(String)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

shops = session.query(Shop).all()
for shop in shops:
    print(shop.name)

session.close()
