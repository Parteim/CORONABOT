import requests
import asyncio
from src.BOT.Groups_methods import Groups


def run():
    bot = Groups(
        'f5f26c4d4e17f59026a331585c2287b1a2613a154fce512c02324f73e432119b51cf37cb7b7ec02b3658a',
    )

    print(bot.connect())


if __name__ == '__main__':
    run()