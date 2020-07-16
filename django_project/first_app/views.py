from django.shortcuts import render
from django.http import HttpResponse
from .models import Item
from .flipkart_root import Scrapper_flipkart
from .Amazon_scrapper import Scrapper_amazon
import threading
import time

def index(request):
    return render(request,"index.html")

def Amazon(item_search,r):
    obj = Scrapper_amazon(item_search)
    obj.initialize()
    objs1 = [Item() for i in range(0,1)]
    for (a,b,c,d,e,f,g) in zip(objs1,obj.name_list,obj.rating_list,obj.item_url,obj.img_url,obj.price_list,obj.specs_list):
        a.name = b
        a.rating = c
        a.url = d
        a.img_url = e
        a.price = f
        a.specs = g
    r[0] = objs1

def Flipkart(item_search,r1):
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
    r1[0] = objs2

def result(request):
    start = time.time()

    item_search = request.GET["search_input"]
    #quantity = int(request.GET["quantity"])

    r = {}
    r1 = {}
    p1 = threading.Thread(target=Amazon,args=(item_search,r))
    p2 = threading.Thread(target=Flipkart, args=(item_search,r1))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
    O1 = r[0]
    O2 = r1[0]
    r.clear()
    r1.clear()
    finish = time.time()
    print()
    print(f'            Finished in {round(finish - start)} seconds'           )
    print()
    return render(request,"result.html",{'item1':O1,'item2':O2})
