import requests
from src.BOT.Groups_methods import Groups


def run():
    bot = Groups(
        '',
    )

    print(bot.connect())


if __name__ == '__main__':
    run()
