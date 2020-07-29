from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class Scrapper_paytm_mobile:
    URL = 'https://paytmmall.com/shop/search?q=' #  iphone%7

    def __init__(self, searchterm):
        self.name_list = list()
        self.price_list = list()
        self.item_url = list()
        self.searchterm = searchterm
        self.URL = self.URL + self.create_url(self.searchterm )
        self.response = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.response.content, 'lxml')

    def create_url(self, searchterm ):
        string_list = searchterm.split(' ')
        new_string = ''
        for i in string_list:
            new_string = new_string + i + '%'
        return new_string[:-1]+"&from=organic&child_site_id=6&site_id=2&category=66781&brand=1707"


    def initialize(self):
        if self.response.status_code == 200:
            return self.get_product_info()
        else:
            print('Request timed out, Poor connection.Try again.')

    def get_product_info(self):
        try:
            for var in self.soup.find_all("div", class_='_2i1r'):
                if len(self.name_list) == 1:
                    break

                if var.find('div', class_ ='UGUy') is None:
                    self.name_list.append("Item not found")
                else:
                    name = var.find('div', {'class': 'UGUy'}).get_text()
                    self.name_list.append(name)

                if var.find('div', class_ ='_1kMS') is not None:
                    price = var.find('div', class_ ='_1kMS').get_text()
                    self.price_list.append("₹ "+price)

                itemurl = var.find('a', {'class': '_8vVO'}).get('href')
                self.item_url.append("https://paytmmall.com/"+itemurl)

            if len(self.name_list) == 0:
                self.name_list.append("Not avaliable !")
                self.price_list.append(" ")
                self.item_url.append(" ")

        except:
            print('Class name is different')

    def notFound(self):
        pass
        #print('System Error!')


class Scrapper_paytm_laptop:
    URL = 'https://paytmmall.com/shop/search?q=' #  iphone%7

    def __init__(self, searchterm):
        self.name_list = list()
        self.price_list = list()
        self.item_url = list()
        self.searchterm = searchterm
        self.URL = self.URL + self.create_url(self.searchterm )
        self.response = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.response.content, 'lxml')

    def create_url(self, searchterm ):
        string_list = searchterm.split(' ')
        new_string = ''
        for i in string_list:
            new_string = new_string + i + '%'
        return new_string[:-1]+"&from=organic&child_site_id=1&site_id=1"


    def initialize(self):
        if self.response.status_code == 200:
            return self.get_product_info()
        else:
            print('Request timed out, Poor connection.Try again.')

    def get_product_info(self):
        try:
            for var in self.soup.find_all("div", class_='_2i1r'):
                if len(self.name_list) == 1:
                    break

                if var.find('div', class_ ='UGUy') is None:
                    self.name_list.append("Item not found")
                else:
                    name = var.find('div', {'class': 'UGUy'}).get_text()
                    self.name_list.append(name)

                if var.find('div', class_ ='_1kMS') is not None:
                    price = var.find('div', class_ ='_1kMS').get_text()
                    self.price_list.append("₹ "+price)

                itemurl = var.find('a', {'class': '_8vVO'}).get('href')
                self.item_url.append("https://paytmmall.com/"+itemurl)

            if len(self.name_list) == 0:
                self.name_list.append("Not avaliable !")
                self.price_list.append(" ")
                self.item_url.append(" ")

        except:
            print('Class name is different')

    def notFound(self):
        pass
        #print('System Error!')
