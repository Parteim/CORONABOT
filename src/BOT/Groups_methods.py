import requests

from src.BOT.Base import BaseClass
from src.BOT.Messages_methods import Message


class Groups(BaseClass):
    def __init__(self, token):
        super().__init__(token)
        self.url += '/groups'

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
            print(receiver)

            update = receiver['updates']
            print(update)

            if update:
                for i in update:
                    if i['type'] == 'message_new':
                        obj = i['object']
                        message.mark_as_read(
                            # [obj['id']],                                  # message ids
                            peer_id=obj['user_id'],                         # peer id
                            # start_message_id=obj['id'],                   # start message id
                            group_id=i['group_id'],                         # group id
                        )

                        message_body = message.check_prefix(i['object']['body'])

                        print(message_body)

                        if message_body:
                            message.send(
                                message_body,                                       # message body
                                peer_id=obj['user_id']                      # receiver
                            )
            ts = receiver['ts']

