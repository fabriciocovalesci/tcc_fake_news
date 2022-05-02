#!/usr/bin/env python3

import re
import requests
from bs4 import BeautifulSoup
import asyncio
import json

from .portal_r7_bot import PortalR7Bot
from .uol_bot import UolBot

class ActaBot:
    
    def __init__(self):
        self.obj_scraping = []
        
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
        