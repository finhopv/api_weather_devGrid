import asyncio
import pytest
from tasks import fetch_weather_data
from models import UserRequest
from database import SessionLocal

@pytest.mark.asyncio
async def test_fetch_weather_data():
    # Cria uma nova sessão
    session = SessionLocal()

    try:
        user_request = UserRequest(user_id="testa102", total_cities=1)
        session.add(user_request)
        session.commit()

        await fetch_weather_data("test10", [3443280, 3443289, 3443342, 3443356, 3443588], session)
        assert session.query(UserRequest).get("test10").completed_cities == 1
    finally:
        # Fecha a sessão
        session.close()

async def main():
    weather_data = await test_fetch_weather_data()
    print(weather_data)

# Executar a função principal
if __name__ == "__main__":
    asyncio.run(main())
