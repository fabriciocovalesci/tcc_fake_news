#!/usr/bin/env python3

from Bots.acta_bot import ActaBot
from Bots.uol_bot import UolBot


def main():
    bot = ActaBot(['https://www.portalbr7.com/', 'https://www.uol.com.br/'])
    bot.start()
    
if __name__ == "__main__":
    print(main())