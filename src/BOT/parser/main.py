import requests
from bs4 import BeautifulSoup


def receive(url):
    html_page = requests.get(url)

    soup = BeautifulSoup(html_page.content, 'html.parser')

    counters = soup.find_all('div', class_='maincounter-number', limit=2)

    infected = counters[0].find('span').text

    deaths = counters[1].find('span').text

    # print(counters[1])

    print(f'infected: {infected} \ndeaths: {deaths}')


receive(
    'https://www.worldometers.info/coronavirus/'
)