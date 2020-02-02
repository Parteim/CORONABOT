import requests
from src.BOT.parser.main import parse
from src.BOT.Base import BaseClass


class Message(BaseClass):
    def __init__(self, token):
        super().__init__(token)
        self.url += '/messages'

    def check_prefix(self, message):
        # reserved_words = {
        #     'Hi': [
        #         'hi',
        #         'Hi',
        #         'Привет',
        #         'привет',
        #         'Здравствуй',
        #         'здравствуй',
        #         'Даров',
        #         'даров',
        #     ],
        #     'status': 'status',
        # }

        print(message[0])
        if message[0] == '.':
            split_message = message.split('.')
            if message == '.hi':
                return 'Привет.\nUntil are live.'
            elif message == '.status':
                return str(parse())
        return False

    def mark_as_read(self, **kwargs):
        url = f'{self.url}.markAsRead'

        response = super().request(url, **kwargs)
        print('complete')
        return response.json()

    def send(self, message, **kwargs):
        url = f'{self.url}.send'

        if 'attachment' not in kwargs:
            kwargs.update(
                message=message,
            )

        response = super().request(url, **kwargs)
        print(response.json())
        return response.json()