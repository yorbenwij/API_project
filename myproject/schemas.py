from pydantic import BaseModel


class PeopleBase(BaseModel):
    surname: str
    lastname: str
    email: str

class PeopleCreate(PeopleBase):
    pass

class People(PeopleBase):
    id: int
    country_id: int

    class Config:
        orm_mode = True

class CountryBase(BaseModel):
    name: str


class CountryCreate(CountryBase):
    population: int

class Country(CountryBase):
    id: int
    civilians: list[People] = []

    class Config:
        orm_mode = True