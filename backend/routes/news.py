from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from models.news import News, Domain
from config.database import db
from schemas.news import newsEntity, oneOrManyNewsEntity, predictNewsEntity, createNewEntity
from datetime import datetime
import json

new = APIRouter()

@new.get('/')
async def find_all_news():
    return {"Hello": "World"} 


@new.get("/news/all")
async def get_all_news():
    return newsEntity(db.collection("news").get())


@new.get("/news/domain/{domain}")
async def find_domain_news(domain):
    domains = {
        "uol": "https://www.uol.com.br/",
        "portalr7": "https://www.portalbr7.com/"
    }
    return newsEntity(db.collection("news").where("domain", "==", domains.get(domain)).get())


@new.get("/news/date/{date}")
async def find_new_date(date):
    date = date.replace("-", "/")
    return newsEntity(db.collection("news").where("date", "==", date).get())


@new.get("/news/date/{date}/{number}")
async def find_new_date_item(date, number):
    date = date.replace("-", "/")
    return oneOrManyNewsEntity(db.collection("news").where("date", "==", date).get(), int(number))


@new.get("/news/predict/{date}")
async def predict_news(date):
    date = date.replace("-", "/")
    return predictNewsEntity(db.collection("news").where("date", "==", date).get())


@new.post("/news/predict")
async def create_news(news: News):
    return createNewEntity(jsonable_encoder(news))