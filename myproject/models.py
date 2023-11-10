from sqlalchemy import Integer, Column, String, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Country(Base):
    __tablename__ = "countries"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    population = Column(Integer, index=True)

    civilians = relationship("People", back_populates="country")


class People(Base):
    __tablename__ = "civilians"

    id = Column(Integer, primary_key=True, index=True)
    surname = Column(String, unique=True, index=True)
    lastname = Column(String, unique=True, index=True)
    email = Column(String, unique=True, index=True)
    country_id = Column(Integer, ForeignKey("countries.id"))

    country = relationship("Country", back_populates="civilians")
