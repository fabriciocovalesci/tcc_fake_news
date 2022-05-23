#!/usr/bin/env python3

import re
import os
from bs4 import BeautifulSoup
import asyncio
import requests
import json

from .database import DataBase
from .portal_r7_bot import PortalR7Bot
from .uol_bot import UolBot

class ActaBot:
    
    def __init__(self):
        self.obj_scraping = []
        self.db = DataBase()
        
    def start(self):
        
        # First Bot
        try:
            portal_bot = PortalR7Bot()
            obj_scraping_portal = asyncio.run(portal_bot.get_text())
            self.obj_scraping.append(obj_scraping_portal)
        except Exception as err:
            print(f"ERROR: Exection BOT [PortalR7Bot] : {err}")
        
        # Second Bot
        try:
#            pass
            uol_bot = UolBot()
            obj_scraping_uol = asyncio.run(uol_bot.get_text())
            self.obj_scraping.append(obj_scraping_uol)
        except Exception as err:
            print(f"ERROR: Exection BOT [UOL] : {err}")
        
        # Third Bot
        try:
            pass
        except Exception as err:
            print(f"ERROR: Exection BOT [] : {err}")
        
        # Fourth Bot
        try:
            pass
        except Exception as err:
            print(f"ERROR: Exection BOT [] : {err}")

        return self.obj_scraping
    
    def show(self):
        json_object = json.dumps(self.obj_scraping, indent=4, ensure_ascii=False) 
        print(json_object)
        
    def send_news(self):
        try:
            host = "http://3.91.38.127/create/news/predict"
            data = {
                "data": self.obj_scraping[0] + self.obj_scraping[1]
                } 
            res = requests.post(url=host, data=json.dumps(data, ensure_ascii=True))
            print(f"Status {res.status_code}")
        except Exception as err:
            print(f"ERROR: send_news() | {err}")
                
    def insert_data_base(self):
        if len(self.obj_scraping[0]) != 0:
            for item in self.obj_scraping[0]:
                try:
                    self.db.data_base.collection('news').add(item)
                except Exception as err_db:
                    print(f"ERROR - Acta Bot - insert Portal R7: function [insert_data_base()] : {err_db}")
                    
        if len(self.obj_scraping[1]) != 0:
            for item in self.obj_scraping[1]:
                try:
                    self.db.data_base.collection('news').add(item)
                except Exception as err_db:
                    print(f"ERROR - Acta Bot - insert UOL: function [insert_data_base()] : {err_db}")
        