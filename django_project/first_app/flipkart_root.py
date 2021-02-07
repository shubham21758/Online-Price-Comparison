from bs4 import BeautifulSoup
import requests

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

def GET_UA():
    uastrings = [
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.72 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10) AppleWebKit/600.1.25 (KHTML, like Gecko) Version/8.0 Safari/600.1.25", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", \
        "Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.111 Safari/537.36", \
        "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5) AppleWebKit/600.1.17 (KHTML, like Gecko) Version/7.1 Safari/537.85.10", \
        "Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko", \
        "Mozilla/5.0 (Windows NT 6.3; WOW64; rv:33.0) Gecko/20100101 Firefox/33.0", \
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'
        "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/38.0.2125.104 Safari/537.36" \
        ]
class Scrapper_flipkart:

    URL = 'https://www.flipkart.com/search?q='
    PRODUCT_CLASS_DICT = {'name': '_3wU53n',
                          'rating': 'niH0FQ',
                          'rating2': 'hGSR34 _1x2VEC',
                          'rating3': 'hGSR34 _1nLEql',
                          'specs': 'vFw0gD',
                          'price': '_1vC4OE _2rQ-NK',
                          'mrp': '_3auQ3N _2GcJzG', }
    BOX_PRODUCT_CLASS_DICT = {'name': '_2cLu-l',  # <a> class
                              'rating': 'hGSR34 _2beYZw',
                              'rating2': 'hGSR34 _1x2VEC',
                              'rating3': 'hGSR34 _1nLEql',
                              'specs': '_1rcHFq',   # <div> class
                              'price': '_1vC4OE', }

    def __init__(self, searchterm):
        self.name_list = list()
        self.specs_list = list()
        self.price_list = list()
        self.rating_list = list()
        self.item_url = list()
        self.offer_list = list()
        self.searchterm = searchterm
        self.URL = self.URL + self.create_url(self.searchterm)
        self.headers = {'User-Agent': GET_UA()}
        self.response = requests.get(self.URL, headers=self.headers)
        self.soup = BeautifulSoup(self.response.content, 'lxml')

    def create_url(self, searchterm):
        string_list = searchterm.split(' ')
        new_string = ''
        for i in string_list:
            new_string = new_string + i + '+'
        return new_string[:-1]+'&page=1'

    def initialize(self):
        if self.response.status_code == 200:
            return self.check_diplay_type()
        else:
            print('Request timed out, Poor connection.Try again.')

    def check_diplay_type(self):
        return self.get_product_info()
        #
        # for var in self.soup.find_all("div", class_='bhgxx2 col-12-12'):
        #     if var.find('a', {'class': '_2cLu-l'}) is not None:
        #         return self.get_product_info_box()
        #     elif var.find('div', {'div', class_ ='_2pi5LC col-12-12') is not None:
        #         return self.get_product_info()

    def get_product_info_box(self):
        try:
            for var in self.soup.find_all("div", class_='bhgxx2 col-12-12'):
                if len(self.name_list) == 1:
                    break
                if var.find('div',class_='niH0FQ _36Fcw_') is not None :
                    rating = var.find('span',class_='_38sUEc').get_text()
                    self.rating_list.append(rating)
                else:
                    pass

                if var.find('a', {'class': self.BOX_PRODUCT_CLASS_DICT['name']}) is None:
                    pass
                else:
                    name = var.find('a', {'class': self.BOX_PRODUCT_CLASS_DICT['name']}).get_text()
                    self.name_list.append(name)

                if var.find('div', {'class': self.BOX_PRODUCT_CLASS_DICT['specs']}) is not None:
                    specs = var.find('div', {'class': self.BOX_PRODUCT_CLASS_DICT['specs']}).get_text()
                    self.specs_list.append(specs)
                else:
                    self.specs_list.append("Nothing")

                if var.find("div", class_=self.BOX_PRODUCT_CLASS_DICT['price']) is None:
                    pass
                else:
                    price = var.find("div", class_=self.BOX_PRODUCT_CLASS_DICT['price']).get_text()
                    self.price_list.append(price)
                if var.find('a',class_='_2cLu-l') is None:
                    pass
                else:
                    itemlink = var.find('a',class_='_2cLu-l').get('href')
                    itemlink = "https://www.flipkart.com"+itemlink
                    self.item_url.append(str(itemlink))

                if var.find('div', class_='VGWI6T') is None:
                    pass
                else:
                    offer = var.find('div',  class_='VGWI6T').get_text()
                    self.offer_list.append(offer)


        except :
            pass
            #print('Class name is different')

    def get_product_info(self):
        try:
            for var in self.soup.find_all("div", class_='_2pi5LC col-12-12'):
                if len(self.name_list) == 1:
                    break
                if var.find('div', class_='gUuXy-') is not None:
                    rating = var.find('span', class_='_2_R_DZ').get_text()
                    self.rating_list.append(rating)
                else:
                    pass

                if var.find('div', class_='col col-7-12') is None:
                    pass
                else:
                    name = var.find('div', class_='_4rR01T').get_text()
                    self.name_list.append(name)

                if var.find('ul', class_='_1xgFaf') is None:
                    pass
                else:
                    specs = ""
                    for i in var.find_all('li',class_='rgWa7D'):
                        specs = specs + i.get_text() +"*"
                    specs = specs.replace("|","")
                    self.specs_list.append(specs)
                if var.find("div", class_='_25b18c') is None:
                    pass
                else:
                    price = var.find("div", class_='_30jeq3 _1_WHN1').get_text()#[1:].replace(',', '')
                    self.price_list.append(price)
                if var.find('a',class_='_1fQZEK') is None:
                    pass
                else:
                    itemlink = var.find('a',class_='_1fQZEK').get('href')
                    itemlink = "https://www.flipkart.com"+itemlink
                    self.item_url.append(str(itemlink))
                if var.find('div', class_='_2ZdXDB') is not None:
                    offer = var.find('div', class_='_2ZdXDB').get_text()
                    self.offer_list.append(offer)
                # elif var.find('div', class_='VGWI6T') is not None:
                #     offer = var.find('div',class_='VGWI6T').get_text()
                #     self.offer_list.append(offer)
                else:
                    pass

        except :
            pass
            #print('Class name is different')

    def notFound(self):
        pass
        #print('System Error!')
