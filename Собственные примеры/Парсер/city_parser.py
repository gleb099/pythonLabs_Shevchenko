import requests
from bs4 import BeautifulSoup


class Parser:
    URL = "https://geogoroda.ru/strana/rossiya"
    data = []

    temp = list()

    def get_html(self, url, params=None):
        r = requests.get(url, params)
        return r

    def get_content(self, html):
        soup = BeautifulSoup(html, "html.parser")

        items = soup.find_all('tr')

        for item in items:
            value = item.find('h2')
            if value != None:
                value = item.find('h2').get_text()
                self.data.append(value)
        # print(self.data)
        for item in items:
            label = item.find_all('p')
            # print(label)
            self.temp.append(label)
        for i in range(len(self.temp)):
            # print(self.temp[i])
            for j in range(len(self.temp[i])):
                # print()
                print(self.temp[i][j].get_text(), end=', ')
            # print()
            print()
            print()

        return self.data

    def parse(self):
        html = self.get_html(self.URL)
        print(html.status_code)
        if html.status_code == 200:
            return self.get_content(html.text)


p = Parser()
# print(p.parse())
p.parse()