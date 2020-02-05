import requests
import random

from src.BOT.Base import BaseClass
from src.BOT.Messages_methods import Message


class Groups(BaseClass):
    def __init__(self, token):
        super().__init__(token)
        self.url += '/groups'

    def update(self, update, message):
        print(update)
        update = update[0]
        if update['type'] == 'message_new':

            obj = update['object']
            message_obj = update['object']['message']

            message.mark_as_read(
                # [obj['id']],                                  # message ids
                peer_id=message_obj['peer_id'],  # peer id
                # start_message_id=obj['id'],                   # start message id
                group_id=update['group_id'],  # group id
            )

            message_body = False
            if message_obj['text'] != '':
                message_body = message.check_prefix(message_obj['text'])

            # if message_obj['from_id'] == 233055395 and message_obj['text'] != '':
            #     message.edit(
            #         message='...',
            #         message_id=message_obj['conversation_message_id'],
            #         peer_id=message_obj['peer_id'],
            #         group_id=update['group_id'],
            #     )

            if message_body:
                message.send(
                    message_body,  # text of message
                    peer_id=message_obj['peer_id'],  # receiver
                    random_id=random.random()
                )

    def get_long_poll_server(self, group_id, **kwargs):
        url = f'{self.url}.getLongPollServer?group_id={group_id}'
        response = self.request(url, **kwargs)
        return response.json()

    def connect(self):
        group_id = 191538226
        response = self.get_long_poll_server(group_id)['response']
        print(response)
        server = response['server']
        key = response['key']
        ts = response['ts']

        message = Message(
            self.token,
        )

        while True:
            receiver = requests.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=25').json()
            update = receiver['updates']

            if update:
                self.update(update, message)

            ts = receiver['ts']
