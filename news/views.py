from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
# Create your views here.

def index(req):
    allNews = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    res = json.loads(allNews.content)
    return render(req, 'index.html', {'res': res})

def query(req):
    searchRes = {}
    if req.GET:
        query = req.GET.get('query').lower()
        queryNews = requests.get('https://newsapi.org/v2/everything?q='+query+'&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
        searchRes = json.loads(queryNews.content)
        return render(req,'index.html', {'res': searchRes})