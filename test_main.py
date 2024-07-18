
### Testes


import asyncio
import pytest
from httpx import AsyncClient
from  __init__  import create_app
from database import SessionLocal, Base, engine
from models import UserRequest, WeatherData

@pytest.fixture
def client():
    app = create_app()
    Base.metadata.create_all(bind=engine)
    yield app
    Base.metadata.drop_all(bind=engine)

@pytest.mark.asyncio
async def test_post_weather(client):
    async with  AsyncClient(app=client, base_url="http://test") as ac:
        response = await ac.post("/weather", json={"city_ids": [3439525, 3439781]})
    assert response.status_code == 202
    assert 'user_id' in response.json

@pytest.mark.asyncio
async def test_get_weather_progress(client):
    async with AsyncClient(app=client, base_url="http://test") as ac:
        response = await ac.get("/weather/test")
    assert response.status_code == 200
    assert response.json['progress'] == 50

