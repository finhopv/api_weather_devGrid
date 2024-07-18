from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks
from sqlalchemy.orm import Session
#from . import crud, models, schemas
from crud import *
from models import *
from schemas import *
from database import SessionLocal, engine
from tasks import fetch_weather_data
import uuid

Base.metadata.create_all(bind=engine)

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/weather", response_model=UserRequest)
async def create_weather_request(city_ids: list[int], background_tasks: BackgroundTasks, db: Session = Depends(get_db)):
    user_id = str(uuid.uuid4())
    user_request = UserRequestCreate(user_id=user_id, total_cities=len(city_ids))
    create_user_request(db, user_request)
    background_tasks.add_task(fetch_weather_data, user_id, city_ids, db)
    return user_request

@router.get("/weather/{user_id}", response_model=UserRequest)
async def get_weather_progress(user_id: str, db: Session = Depends(get_db)):
    user_request = get_user_request(db, user_id)
    if user_request is None:
        raise HTTPException(status_code=404, detail="User ID not found")
    return user_request

@router.get("/weather_data/{id}", response_model=WeatherData)
async def get_weather_data_(id: str,db: Session = Depends(get_db)):
    user_request = get_weather_data(db, id)
    if user_request is None:
        raise HTTPException(status_code=404, detail="not found")
    return user_request

