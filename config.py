from pydantic import BaseModel
from dotenv import load_dotenv
import os
load_dotenv()

class Settings(BaseModel):
    OPEN_WEATHER_API_KEY: str = os.getenv('SECRET_KEY')
    DATABASE_URL: str = 'sqlite:///./weather.db'
    
    class Config:
        env_file = ".env"