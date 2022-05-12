import random
from classifier.classifier import predict
from config.database import db

def newEntity(item) -> dict:
    return {
        "author": item.get("author"),
        "date":  item.get("date"),
        "domain":  item.get("domain"),
        "status":  item.get("status"),
        "text":  item.get("text"),
        "title":  item.get("title"),
        "url":  item.get("url")
    }
    

def newsEntity(entity) -> dict:
    return [newEntity(item.to_dict()) for item in entity]


def oneOrManyNewsEntity(entity, number) -> list:
    if number == 1:
        item = random.choice([newEntity(item.to_dict()) for item in entity])
    else:
        item = random.choices([newEntity(item.to_dict()) for item in entity], k=number)
    return item

def predictNewsEntity(entity):
    item = random.choice([newEntity(item.to_dict()) for item in entity])
    return predict(item.get('text'))


def createNewEntity(entity):
    result_predict = predict(entity.get('text'))
    # print({{i:str(entity[i]) for i in entity}})
    # author, date, domain, status, text, title, url = dict(*entity)
    # corpus = tuple(*entity)
    # print(author)
    print(result_predict)

    return entity
    
# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]