from pydantic import BaseModel
from datetime import datetime

class WeatherDataBase(BaseModel):
    city_id: int
    temperature: float
    humidity: int

class WeatherDataCreate(WeatherDataBase):
    user_id: str

class WeatherData(WeatherDataBase):
    id: int
    timestamp: datetime

    class Config:
        orm_mode = True

class UserRequestBase(BaseModel):
    user_id: str
    total_cities: int

class UserRequestCreate(UserRequestBase):
    pass

class UserRequest(UserRequestBase):
    completed_cities: int

    class Config:
        orm_mode = True
