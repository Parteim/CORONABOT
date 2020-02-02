import requests


def request():
    url = 'https://api.vk.com/method/users.get?user_id=210700286&v=5.52'
    method = None
    version = None
    domain = None
    
    response = requests.get(
        url,
        params={
            'method': method,
        }
    )
    
    return 


def run():
    pass


if __name__ == '__main__':
    run()