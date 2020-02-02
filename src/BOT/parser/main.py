import requests
from bs4 import BeautifulSoup

url = 'https://www.worldometers.info/coronavirus/'


def parse():
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')

    counters = soup.find_all('div', class_='maincounter-number', limit=2)
    infected = counters[0].find('span').text
    deaths = counters[1].find('span').text

    return f'infected: {infected}\n' \
           f'deaths: {deaths}'