from fastapi import APIRouter
from fastapi import Body, FastAPI
from typing import Union, Optional
from fastapi.encoders import jsonable_encoder
from models.news import News, Domain, OnlyNew, NewsList
from config.database import db
from schemas.news import newsEntity, oneOrManyNewsEntity, predictNewsEntity, createNewEntity, predictNewsEntityHome, predictOnlyNewsEntity
from datetime import datetime
import json

new = APIRouter()

@new.get('/')
async def find_all_news():
    results = db.collection("news").limit(10).get()    
    documents = []
    for item in results:
        doc = db.collection("news").document(item.id)
        data = {
            "author": doc.get().to_dict().get("author"),
            "date":  doc.get().to_dict().get("date"),
            "domain":  doc.get().to_dict().get("domain"),
            "status":  doc.get().to_dict().get("status"),
            "text":  doc.get().to_dict().get("text"),
            "title":  doc.get().to_dict().get("title"),
            "url":  doc.get().to_dict().get('url')
        }
        documents.append(data)
    return {"data": documents }


@new.get("/news/all")
async def get_all_news():
    return newsEntity(db.collection("news").get())


@new.post("/news/only/predict")
def predict_only_news(news: OnlyNew):
    return predictOnlyNewsEntity(jsonable_encoder(news))


@new.get("/news/domain/{domain}")
async def find_domain_news(domain):
    domains = {
        "uol": "https://www.uol.com.br/",
        "portalr7": "https://www.portalbr7.com/"
    }
    return newsEntity(db.collection("news").where("domain", "==", domains.get(domain)).get())


@new.post("/create/news/predict")
async def create_news(data: NewsList):
    return createNewEntity(jsonable_encoder(data))


# @new.get("/news/date/{date}")
# async def find_new_date(date):
#     date = date.replace("-", "/")
#     return newsEntity(db.collection("news").where("date", "==", date).get())


# @new.get("/news/date/{date}/{number}")
# async def find_new_date_item(date, number):
#     date = date.replace("-", "/")
#     return oneOrManyNewsEntity(db.collection("news").where("date", "==", date).get(), int(number))


# @new.get("/news/predict/{date}")
# async def predict_news(date):
#     date = date.replace("-", "/")
#     print(date)
#     return predictNewsEntity(db.collection("news").where("date", "==", date).get())






