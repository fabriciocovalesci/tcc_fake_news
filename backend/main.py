from fastapi import FastAPI
from routes.news import new


app = FastAPI()

app.include_router(new)


# run -> uvicorn main:app --host 127.0.0.1 --port 80

# python3 -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload
