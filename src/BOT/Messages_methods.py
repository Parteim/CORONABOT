import requests
from src.BOT.parser.main import parse
from src.BOT.Base import BaseClass


class Message(BaseClass):
    def __init__(self, token):
        super().__init__(token)
        self.url += '/messages'

    def check_prefix(self, message):
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

    def delete_message(self, **kwargs):
        """
        arg:
        message_ids = [1, 2, 3 , ...]
        group_id
        delete_for_all = 1 or 0 (if the message don't older 24 hours)
        :param kwargs:
        :return: json obj (1 for each of deleted message)
        """

        url = f'{self.url}.delete'

        response = super().request(url, **kwargs)

        return response.json()

    def edit(self, **kwargs):
        """
        arg:
        message (if attach is not true)
        message_id
        peer_id
        group_id
        :param kwargs:
        :return: json obj (1)
        """
        url = f'{self.url}.edit'

        response = super().request(url, **kwargs)

        return response.json()