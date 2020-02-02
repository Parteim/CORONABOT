import requests

from src.BOT.Base import BaseClass


class Message(BaseClass):
    def __init__(self, token, version):
        super().__init__(token, version)
        self.url += '/messages'

    def mark_as_read(self, message_ids, peer_id, start_message_id, group_id, **kwargs):
        url = f'{self.url}.markAsRead?message_ids={message_ids}'

        kwargs.update(
            peer_id=peer_id,
            start_message_id=start_message_id,
            group_id=group_id,
        )

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



