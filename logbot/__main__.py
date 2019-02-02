import os

from .bot import Bot


if __name__ == "__main__":
    bot = Bot(os.getenv("TOKEN"))
    bot.run(host=os.getenv("HOST"), port=int(os.getenv("PORT")))
