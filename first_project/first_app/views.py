from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
# from .Flipkart_scrapper_home import Scrapper_flipkart_home
from .flipkart_root import Scrapper_flipkart
from .Amazon_scrapper import Scrapper_amazon
import multiprocessing
import time
# Create your views here

def index(request):

    # obj = Scrapper_flipkart_home()
    # obj.initialize()
    # objs = [Item() for i in range(0,3)]
    # for (a,b,c,d) in zip(objs,obj.name_list,obj.specs_list,obj.price_list):
    #     a.name = b
    #     a.specs = c
    #     a.price = d
        # a.img_url = e
        # a.url = d

    # item1 = Item_flipkart()
    # item1.name = "Iphone 7"
    # item1.price = 27000
    # item1.rating = 350
    # item1.specs = "3000 Mah battery"
    # item1.imgurl = "https://rukminim1.flixcart.com/image/312/312/k12go7k0/mobile/7/e/e/apple-iphone-7-mn8x2hn-a-original-imafkqcqhzxuvcpd.jpeg?q=70"
    # item1.offer = False

    return render(request,"index.html")

def Amazon(item_search,r):
    obj = Scrapper_amazon(item_search)
    obj.initialize()
    objs1 = [Item() for i in range(0,1)]

    for (a,b,c,d,e,f) in zip(objs1,obj.name_list,obj.rating_list,obj.item_url,obj.img_url,obj.price_list):
        a.name = b
        a.rating = c
        a.url = d
        a.img_url = e
        a.price = f
    r[0] = objs1

def Flipkart(item_search,r1):
    obj = Scrapper_flipkart(item_search)
    obj.initialize()
    objs2 = [Item() for i in range(0,1)]
    for (a,b,c,d,e,f,g) in zip(objs2,obj.name_list,obj.price_list,obj.rating_list,obj.offer_list,obj.item_url,obj.specs_list,):
        a.name = b
        a.price = c
        a.rating = d
        a.offer = e
        a.url = f
        a.specs = g.split('*')
        a.specs.pop()

    r1[0] = objs2

def result(request):
    start = time.time()

    item_search = request.GET["search_input"]
    #quantity = int(request.GET["quantity"])

    manager = multiprocessing.Manager()
    r = manager.dict()
    r1 = manager.dict()

    p1 = multiprocessing.Process(target=Amazon,args=(item_search,r))
    p2 = multiprocessing.Process(target=Flipkart, args=(item_search,r1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()

    O1 = r.values()[0]
    O2 = r1.values()[0]
    # O1 = Amazon(item_search)
    # O2 = Flipkart(item_search)
    finish = time.time()

    print(f'Finished in {round(finish - start)} secounds')
    return render(request,"result.html",{'item1':O1,'item2':O2})
