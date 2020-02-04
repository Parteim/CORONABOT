import requests
import json

# url = 'https://www.worldometers.info/coronavirus/'


class BaseClass():
    def __init__(self, token, version='5.103'):
        self.url = 'https://api.vk.com/method'
        self.token = token
        self.version = version

    def request(self, url, **kwargs):
        params = {
            'v': self.version,
            'access_token': self.token,
        }
        params.update(kwargs)

        response = requests.get(
            url,
            params=params
        )
        return response

    def users_get(self, user_id):
        response = self.request(f'{self.url}/users.get?user_id={user_id}')
        return response.json()