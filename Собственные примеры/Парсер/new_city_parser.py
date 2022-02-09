import requests
from bs4 import BeautifulSoup
import csv

URL = 'https://geogoroda.ru/strana/rossiya'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 YaBrowser/20.7.2.115 Yowser/2.5 Safari/537.36',
    'accept': '*/*'}
HOST = 'https://www.tursvodka.ru'
FILE = 'Townssss.csv'  ## имя файла, файл создастся автоматически при запуске

def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('div',
                      class_='view view-po-stranam view-id-po_stranam view-display-id-page view-dom-id-d6f9b194d3322e44b6da7973b5aa6c0e')
    evens = table.find_all('tr', class_='even')

    town = []  # МАССИВ
    ########################## сверху просто нашли элементы на странице,примитивные №№№№№№№№№№№№№№№№№№№№№№№№№№№№№№

    for even in evens:
        city = even.find('h2').get_text()  ############## GORODA ######
        town.append({'name': city})  ######################################### закидываю переменную в массив по ключу
        nass = even.find_all('p')
        i = 0

        for nas in nass:
            if i == 4:
                nas = nas.get_text()
                nas = nas[23:-8]
            #                print(nas)
            if i == 8:
                nas = nas.get_text()
                nas = nas[:]
            #                print(nas)
            i += 1
    print(town)
    return (town)  ################   возвращаю


########################################################## SAVE IN CSV
def save_file(evens, path):  ## указываем переменную из которой перебираем значения и путь,куда сохраняем
    with open(path, 'w', newline='') as file:  ### открываем файлик
        writer = csv.writer(file, delimiter=';')
        writer.writerow(['GOROD'])  ### подписываем столбец в экселе
        #        print(punkts)
        for even in evens:
            writer.writerow([even['name']])  ### записываем все элементы в один столбец, обратились по ключу


############################################################################

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        towns = []  ### пустой массив
        get_content(html.text)
        towns.extend(get_content(html.text))  ### расширяем пустой массив
        save_file(towns, FILE)  ## вызываем функцию записи в цсв, указываем массив и путь к файлу, файл создастся сам!


    else:
        print('Error')


parse()