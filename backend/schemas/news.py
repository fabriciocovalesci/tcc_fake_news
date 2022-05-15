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

def onlyNewEntity(item) -> dict:
    return {
        "text": item.get("text")
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
    item = [newEntity(item.to_dict()) for item in entity]
    return item

def predictNewsEntityHome(entity):
    item = newEntity(entity)
    return predict(item.get('text'))


def createNewEntity(entity):
    try:
        for item in entity.get('data'):
            item["status"] = predict(item.get('text')).get("modelo")
            db.collection("news").add(item)
        return entity.get('data')
    except Exception as err:
        print(f"ERROR: createNewEntity() | {err}")

def predictOnlyNewsEntity(entity):
    return predict(onlyNewEntity(entity).get('text'))
    
# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

# def serializeList(entity) -> list:
#     return [serializeDict(a) for a in entity]