#!/usr/bin/env python3

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
from routes.news import new


app = FastAPI(
    title="API Fake News",
    openapi_url="/openapi.json",
    version="1.0.0",
)

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(new)


HOST = "3.91.38.127"
HOST = "localhost"
PORT = 8000

# run -> uvicorn main:app --host 127.0.0.1 --port 80

# python3 -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

if __name__ == '__main__':

    import uvicorn
    
    uvicorn.run(app,  # type: ignore
        port= PORT,
        host= HOST,
        use_colors=True,
        debug=False,
        )


"""
/ GET 
    -> Exibir 5 noticias fakes e verdadeiras do dia anterior baseado na maior probabilidade
    -> Exibir graficamente estatisticas baseados na quantidade de noticias fake ou verdadeiras
    
/predict POST -> Envio de noticia para verificar a sua autenticidade
/predict/link POST -> Envio de link (Raspagem de dados e apos verificar se noticia é Fake ou Verdadeira) 

"""
