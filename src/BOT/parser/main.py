import requests
from bs4 import BeautifulSoup
from datetime import date

url = 'https://www.worldometers.info/coronavirus/'


def difference():

    def str_to_int(string):
        if split_str[0] == string:
            i = split_str[0]
            try:
                i = split_str[1].split(',')
                i = i[0] + i[1]
            except:
                pass
            return int(i[0])
        return False

    with open('data.txt', 'r') as file:
        infected = None
        deaths = None
        recovered = None
        for line in file.readlines():
            split_str = line.split(' ')
            print(split_str)

            checker = str_to_int('infected:')
            if checker:
                infected = checker

            checker = str_to_int('deaths:')
            if checker:
                deaths = checker

            checker = str_to_int('recovered:')
            if checker:
                recovered = checker

    file.close()
    return f'infected: {infected}'


def parse():
    html_page = requests.get(url)
    soup = BeautifulSoup(html_page.content, 'html.parser')

    clock = date.today()

    date_str = f'{clock.day}.{clock.month}.{clock.year}'
    print(clock)

    counters = soup.find_all('div', class_='maincounter-number', limit=3)
    infected = counters[0].find('span').text
    deaths = counters[1].find('span').text
    recovered = counters[2].find('span').text

    return f'date {date_str} \n' \
           f'infected --- {infected} \n' \
           f'deaths ---{deaths} \n' \
           f'recovered --- {recovered} \n'


def writer():
    with open('data.txt', 'w') as file:
        file.writelines(
            parse()
        )
    file.close()
    return 1


if __name__ == '__main__':
    difference()