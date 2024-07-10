from fastapi import FastAPI
from quiz_backend.db.db_connector import get_session , create_table
from contextlib import asynccontextmanager
from quiz_backend.models.user_models import User
import quiz_backend.models.admin_models
import quiz_backend.models.quiz_models


@asynccontextmanager
async def lifeSpan(app: FastAPI):
    create_table()
    print("create table....")
    yield


app = FastAPI(lifespan=lifeSpan)

@app.get('/')
def home():
    return "Welcome to Quiz app project"