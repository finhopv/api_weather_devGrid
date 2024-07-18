from fastapi import FastAPI
from config import Settings
from models import *
from database import engine

settings = Settings()

def create_app():
    app = FastAPI()

    Base.metadata.create_all(bind=engine)

    from main import router
    app.include_router(router)

    return app
create_app()