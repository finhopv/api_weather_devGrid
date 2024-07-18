from sqlalchemy import Column, Integer, String, Float, DateTime
from database import Base
from datetime import datetime

class WeatherData(Base):
    __tablename__ = 'weather_data'

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(String, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    city_id = Column(Integer)
    temperature = Column(Float)
    humidity = Column(Integer)

class UserRequest(Base):
    __tablename__ = 'user_requests'

    user_id = Column(String, primary_key=True, index=True)
    total_cities = Column(Integer)
    completed_cities = Column(Integer, default=0)

WeatherData()
UserRequest()