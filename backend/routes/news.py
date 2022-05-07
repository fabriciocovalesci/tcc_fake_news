from fastapi import APIRouter
from models.news import News, Domain
from config.database import db
from schemas.news import newsEntity, oneOrManyNewsEntity
from datetime import datetime


new = APIRouter()

@new.get('/')
async def find_all_news():
    return {"Hello": "World"} 


@new.get("/news/all")
async def all_news():
    return newsEntity(db.collection("news").get())


@new.get("/news/domain/{domain}")
async def domain_news(domain):
    domains = {
        "uol": "https://www.uol.com.br/",
        "portalr7": "https://www.portalbr7.com/"
    }
    return newsEntity(db.collection("news").where("domain", "==", domains.get(domain)).get())


@new.get("/news/date/{date}")
async def domain_news(date):
    date = date.replace("-", "/")
    return newsEntity(db.collection("news").where("date", "==", date).get())


@new.get("/news/date/{date}/{number}")
async def domain_news(date, number):
    date = date.replace("-", "/")
    return oneOrManyNewsEntity(db.collection("news").where("date", "==", date).get(), int(number))