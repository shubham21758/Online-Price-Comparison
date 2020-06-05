from bs4 import BeautifulSoup
import requests

# headers = {'User-Agent': 'chrome'}
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

class Scrapper_flipkart_home:
    URL = 'https://www.flipkart.com/mobile-phones-store?otracker=nmenu_sub_Electronics_0_Mobiles'

    def __init__(self):
        self.name_list = list()
        self.specs_list = list()
        self.price_list = list()
        self.item_url = list()
        self.img_url = list()
        self.response = requests.get(self.URL, headers=headers)
        self.soup = BeautifulSoup(self.response.content, 'lxml')
        # if self.noitems == 0:
        #     print('not valid input')
        #     exit()

    def initialize(self):
        if self.response.status_code == 200:
            # print('Scraping initiated for search: ', self.searchterm)
            return self.get_product_info()
        else:
            print('Request timed out, Poor connection.Try again.')

    def get_product_info(self):
        try:
            for var in self.soup.find_all("div", class_='_2kSfQ4'):
                if len(self.name_list) == 4:
                    break
                if var.find('div', class_='iUmrbN') is not None:
                    name = var.find('div', class_='iUmrbN').get_text()
                    self.name_list.append(name)
                else:
                    pass
                if var.find('div',class_='BXlZdc') is None:
                    pass
                else:
                    specs = var.find('div',class_='BXlZdc').get_text()
                    self.specs_list.append(specs)
                if var.find('div',class_='M_qL-C') is None:
                    pass
                else:
                    price = var.find('div',class_='M_qL-C').get_text()
                    self.price_list.append(price)
                
                # for image in self.soup.findAll('img'):
                #     img = image.get('src')
                #     print(img)
                #     print()
                #     self.img_url.append(img)
                # if len(self.img_url) !=0:
                #     self.img_url.pop(0)


        except :
            pass
            #print('Class name is different')

    def notFound(self):
        pass
        #print('System Error!')
