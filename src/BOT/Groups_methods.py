import requests

from src.BOT.Base import BaseClass
from src.BOT.Messages_methods import Message


class Groups(BaseClass):
    def __init__(self, token, version):
        super().__init__(token, version)
        self.url += '/groups'

    def check_prefix(self, message):
        print(message[0])
        if message[0] == '.':
            return True

        return False

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
            self.version,
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
                            [obj['id']],
                            obj['user_id'],
                            obj['id'],
                            i['group_id'],
                        )
                        print('mark as read', -group_id)
                        if self.check_prefix(i['object']['body']):
                            message.send(
                                'hi',
                                peer_id=obj['user_id']
                            )

            ts = receiver['ts']


bot = Groups(
    'f5f26c4d4e17f59026a331585c2287b1a2613a154fce512c02324f73e432119b51cf37cb7b7ec02b3658a',
    '5.52',
)

print(bot.connect())
