

from Bots.ActaBot.acta_bot import ActaBot


def main():
    bot = ActaBot(['https://www.portalbr7.com/', 'www.google.com/'])
    bot.get_domain()
    
    
if __name__ == "__main__":
    print(main())