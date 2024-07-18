from models import UserRequest, WeatherData


def test_weather_data_model():
    weather_data = WeatherData(
        user_id="test",
        city_id=123,
        temperature=25.5,
        humidity=80
    )
    assert weather_data.user_id == "test"
    assert weather_data.city_id == 123
    assert weather_data.temperature == 25.5
    assert weather_data.humidity == 80

def test_user_request_model():
    user_request = UserRequest(
        user_id="test",
        total_cities=10,
        completed_cities=5
    )
    assert user_request.user_id == "test"
    assert user_request.total_cities == 10
    assert user_request.completed_cities == 5
test_weather_data_model()