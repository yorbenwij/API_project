from sqlalchemy.orm import Session

import models
import schemas


def get_country(db: Session, country_id: int):
    return db.query(models.Country).filter(models.Country.id == country_id).first()


def get_country_by_name(db: Session, name: str):
    return db.query(models.Country).filter(models.Country.name == name).first()


def get_countries(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Country).offset(skip).limit(limit).all()

def create_country(db: Session, country: schemas.CountryCreate):
    db_Country = models.Country(name=country.name, population=country.population)
    db.add(db_Country)
    db.commit()
    db.refresh(db_Country)
    return db_Country


def get_civilians(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.People).offset(skip).limit(limit).all()

def create_country_civilians(db: Session, civilians: schemas.PeopleCreate, country_id: int):
    db_people = models.People(**civilians.dict(), country_id=country_id)
    db.add(db_people)
    db.commit()
    db.refresh(db_people)
    return db_people

