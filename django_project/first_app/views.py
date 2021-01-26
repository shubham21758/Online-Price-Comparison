from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .flipkart_root import Scrapper_flipkart
from .Amazon_scrapper import Scrapper_amazon
from .paytm_scrapper import *
import threading
import time

def index(request):
    return render(request,"index.html")

def Amazon(item_search,amazon_obj):
    obj = Scrapper_amazon(item_search)
    obj.initialize()
    objs1 = [Item() for i in range(0,1)]
    for (a,b,c,d,e,f,g) in zip(objs1,obj.name_list,obj.rating_list,obj.item_url,obj.img_url,obj.price_list,obj.specs_list):
        a.name = b
        a.rating = c
        a.url = d
        a.img_url = e
        print(a.img_url)
        a.price = f
        a.specs = g
    amazon_obj[0] = objs1

def Flipkart(item_search,flipkart_obj):
    obj = Scrapper_flipkart(item_search)
    obj.initialize()
    objs2 = [Item() for i in range(0,1)]
    for (a,b,c,d,e,f,g) in zip(objs2,obj.name_list,obj.price_list,obj.rating_list,obj.offer_list,obj.item_url,obj.specs_list):
        a.name = b
        a.price = c
        a.rating = d
        a.offer = e
        a.url = f
        a.specs = g.split('*')
        a.specs.pop()
    flipkart_obj[0] = objs2

def Paytm(item_search,paytm_obj,category):
    if category =="Mobiles":
        obj = Scrapper_paytm_mobile(item_search)
        obj.initialize()
    else:
        obj = Scrapper_paytm_laptop(item_search,)
        obj.initialize()

    objs3 = [Item() for i in range(0,1)]
    for (a,b,c,d) in zip(objs3,obj.name_list,obj.price_list,obj.item_url):
        a.name = b
        a.price = c
        a.url = d
    paytm_obj[0] = objs3

def result(request):
    start = time.time()

    item_search = request.GET["search_input"]
    try:
        category = request.GET["dropdown"]
    except:
        category = "Mobiles"

    amazon_obj = {}
    flipkart_obj = {}
    paytm_obj = {}

    t1 = threading.Thread(target=Amazon,args=(item_search,amazon_obj))
    t2 = threading.Thread(target=Flipkart, args=(item_search,flipkart_obj))
    t3 = threading.Thread(target=Paytm, args=(item_search,paytm_obj,category))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    O1 = amazon_obj[0]
    O2 = flipkart_obj[0]
    O3 = paytm_obj[0]

    amazon_obj.clear()
    flipkart_obj.clear()
    paytm_obj.clear()

    finish = time.time()
    print()
    print(f'            Finished in {round(finish - start)} seconds'           )
    print()
    return render(request,"result.html",{'item1':O1,'item2':O2,'item3':O3})
