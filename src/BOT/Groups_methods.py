import requests

from src.BOT.Base import BaseClass


class Groups(BaseClass):
    def __init__(self, token, version):
        super().__init__(token, version)

    def get_long_poll_server(self, group_id, **kwargs):
        url = f'{self.url}/groups.getLongPollServer?group_id={group_id}'
        response = self.request(url, **kwargs)
        return response.json()

    def connect(self):
        response = self.get_long_poll_server(191538226)['response']
        print(response)
        server = response['server']
        key = response['key']
        ts = response['ts']

        while True:
            receiver = requests.get(f'{server}?act=a_check&key={key}&ts={ts}&wait=25').json()
            print(receiver)

            update = receiver['updates']
            print(update)

            if update:
                for i in update:
                    print(i)
            ts = receiver['ts']


bot = Groups(
    'f5f26c4d4e17f59026a331585c2287b1a2613a154fce512c02324f73e432119b51cf37cb7b7ec02b3658a',
    '5.52',
)

print(bot.connect())
