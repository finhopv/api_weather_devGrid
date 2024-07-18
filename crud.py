from sqlalchemy.orm import Session
from models import UserRequest, WeatherData
from schemas import UserRequestCreate, WeatherDataCreate


def create_user_request(db: Session, user_request: UserRequestCreate):
    db_user_request = UserRequest(**user_request.dict())
    db.add(db_user_request)
    db.commit()
    db.refresh(db_user_request)
    return db_user_request

def get_user_request(db: Session, user_id: str):
    return db.query(UserRequest).filter(UserRequest.user_id == user_id).first()

def update_user_request(db: Session, user_id: str, completed_cities: int):
    db_user_request = db.query(UserRequest).filter(UserRequest.user_id == user_id).first()
    db_user_request.completed_cities = completed_cities
    db.commit()
    db.refresh(db_user_request)
    return db_user_request

def create_weather_data(db: Session, weather_data: WeatherDataCreate):
    db_weather_data = WeatherData(**weather_data.dict())
    db.add(db_weather_data)
    db.commit()
    db.refresh(db_weather_data)
    return db_weather_data

def get_weather_data(db: Session, id: str):
    return db.query(WeatherData).filter(WeatherData.id == id).first()

