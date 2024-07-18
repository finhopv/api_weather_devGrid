import asyncio
import httpx
#from . import crud, schemas
from crud import create_user_request,get_user_request, create_weather_data, update_user_request
from schemas import *
from sqlalchemy.orm import Session
from dotenv import load_dotenv
import os

load_dotenv()
async def fetch_weather_data(user_id: str, city_ids: list[int], db: Session):
    api_key = os.getenv('SECRET_KEY')
    url = "https://api.openweathermap.org/data/2.5/weather"

    async def fetch(city_id):
        async with httpx.AsyncClient() as client:
            response = await client.get(url, params={"id": city_id, "appid": api_key})
            data = response.json()
            print(data)
            weather_data = WeatherDataCreate(
                user_id=user_id,
                city_id=city_id,
                temperature=data["main"]["temp"],
                humidity=data["main"]["humidity"]
            )
            create_weather_data(db, weather_data)
            user_request = get_user_request(db, user_id)
            update_user_request(db, user_id, user_request.completed_cities + 1)

    tasks = []
    for city_id in city_ids:
        tasks.append(fetch(city_id))
    await asyncio.gather(*tasks)

