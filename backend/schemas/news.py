import random

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

# def serializeDict(a) -> dict:
#     return {**{i:str(a[i]) for i in a if i=='_id'},**{i:a[i] for i in a if i!='_id'}}

def serializeList(entity) -> list:
    return [serializeDict(a) for a in entity]