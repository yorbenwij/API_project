from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from database import SessionLocal, engine
import os
import schemas
import crud
import models
if not os.path.exists('.\sqlitedb'):
    os.makedirs('.\sqlitedb')

#"sqlite:///./sqlitedb/sqlitedata.db"
models.Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.post("/countries/", response_model=schemas.Country)
def create_country(country: schemas.CountryCreate, db: Session = Depends(get_db)):
    db_country = crud.get_country_by_name(db, name=country.name)
    if db_country:
        raise HTTPException(status_code=400, detail="Country already registered")
    return crud.create_country(db=db, country=country)

@app.get("/countries/", response_model=list[schemas.Country])
def read_countries(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    countries = crud.get_countries(db, skip=skip, limit=limit)
    return countries

@app.get("/countries/{country_id}", response_model=schemas.Country)
def read_country(country_id: int, db: Session = Depends(get_db)):
    db_country = crud.get_country(db, country_id=country_id)
    if db_country is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_country

@app.post("/countries/{country_id}/civilians/", response_model=schemas.People)
def create_country_civilians(
        country_id: int, civilian: schemas.PeopleCreate, db: Session = Depends(get_db)
):
    return crud.create_country_civilians(db=db, civilians=civilian, country_id=country_id)

@app.get("/civilians/", response_model=list[schemas.People])
def read_civilians(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    civilians = crud.get_civilians(db, skip=skip, limit=limit)
    return civilians