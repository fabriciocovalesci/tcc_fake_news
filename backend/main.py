#!/usr/bin/env python3

from fastapi import FastAPI
import uvicorn
from routes.news import new


app = FastAPI(
    title="API Fake News",
    openapi_url="/openapi.json",
    version="1.0.0",
)

app.include_router(new)


HOST = "127.0.0.1"
PORT = 8000

# run -> uvicorn main:app --host 127.0.0.1 --port 80

# python3 -m uvicorn main:app --host 127.0.0.1 --port 8000 --reload

# if __name__ == '__main__':

    # import uvicorn
    
    # uvicorn.run(app,  # type: ignore
    #     "port"= PORT,
    #     "host"= HOST,
    #     # use_colors=True,
    #     "reload"= True,
    #     "workers"=2,
    #     # debug=True,
    #     )


"""
/ GET 
    -> Exibir 5 noticias fakes e verdadeiras do dia anterior baseado na maior probabilidade
    -> Exibir graficamente estatisticas baseados na quantidade de noticias fake ou verdadeiras
    
/predict POST -> Envio de noticia para verificar a sua autenticidade
/predict/link POST -> Envio de link (Raspagem de dados e apos verificar se noticia é Fake ou Verdadeira) 

"""
