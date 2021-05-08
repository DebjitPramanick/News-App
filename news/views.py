from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
# Create your views here.

countries = {'ae': 'UAE', 'ar': 'Argentina', 'at': 'Austria', 'au': 'Australia', 'be': 'Belgium', bg br ca ch cn co cu cz de eg fr gb gr hk hu id ie il in it jp k rl tl vm am xm yn gn ln on zp hp lp tr or sr us as es gs is kt ht rt wu au sv ez}



def index(req):
    
    allNews = requests.get('https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    res = json.loads(allNews.content)
    return render(req, 'index.html', {'res': res})

def query(req):
    searchRes = {}
    if req.GET:
        query = req.GET.get('query').lower()
        queryNews = requests.get('https://newsapi.org/v2/everything?q='+query+'&pageSize=100&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
        searchRes = json.loads(queryNews.content)
        return render(req,'index.html', {'res': searchRes})

def getCategory(req, ct):
    searchRes = {}
    catNews = requests.get('https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category='+ct+'&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    searchRes = json.loads(catNews.content)
    return render(req,'index.html', {'res': searchRes})