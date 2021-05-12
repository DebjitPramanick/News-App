from django.shortcuts import render
import requests
import json
from django.http import JsonResponse
# Create your views here.

countries = {'ae': 'UAE', 'ar': 'Argentina', 
'at': 'Austria', 'au': 'Australia', 
'be': 'Belgium', 'bg': 'Bulgaria', 
'br': 'Brazil', 'ca': 'Canada', 
'ch': 'Switzerland', 'cn': 'China', 
'co': 'Colombia', 'cu': 'Cuba', 
'cz': 'Czech Republic', 'de': 'Germany', 
'eg': 'Egypt', 'fr': 'France', 
'gb': 'United Kingdom', 'gr': 'Greece', 
'hk': 'Hong Kong', 'hu': 'Hungary', 
'id': 'Indonesia', 'ie': 'Ireland',
'il': 'Israel', 'in': 'India',
'it': 'Italy', 'jp': 'Japan',
'kr': 'South Korea', 'lt': 'Lithuania',
'lv': 'Latvia', 'ma': 'Morocco',
'mx': 'Mexico', 'my': 'Malaysia',
'ng': 'Nigeria', 'nl': 'Netherlands',
'no': 'Norway', 'nz': 'New Zealand',
'ph': 'Philippines', 'pl': 'Poland',
'pt': 'Portugal', 'ro': 'Romania',
'rs': 'Serbia', 'ru': 'Russia',
'sa': 'Saudi Arabia', 'se': 'Sweden',
'sg': 'Singapore', 'si': 'Slovenia',
'sk': 'Slovakia', 'th': 'Thailand',
'tr': 'Turkey', 'tw': 'Taiwan',
'ua': 'Ukraine', 'us': 'United States',
've': 'Venezuela', 'za': 'South Africa'}



def index(req):
    print(countries['hk'])
    allNews = requests.get('https://newsapi.org/v2/top-headlines?country=in&pageSize=100&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    res = json.loads(allNews.content)

    for r in res['articles']:
        if r['author'] == None: r['author'] = 'Unknown'
        if r['urlToImage'] == None: r['urlToImage'] = 'Unknown'
        if r['description'] == None: r['description'] = 'Unknown'
        if r['content'] == None: r['content'] = 'Unknown'
        if r['source']['id'] == None: r['source']['id'] = 'Unknown'

    return render(req, 'index.html', {'res': res , 'cou': countries.items()})

def query(req):
    searchRes = {}
    if req.GET:
        query = req.GET.get('query').lower()
        queryNews = requests.get('https://newsapi.org/v2/everything?q='+query+'&pageSize=100&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
        searchRes = json.loads(queryNews.content)
        for r in searchRes['articles']:
            if r['author'] == None: r['author'] = 'Unknown'
            if r['urlToImage'] == None: r['urlToImage'] = 'Unknown'
            if r['description'] == None: r['description'] = 'Unknown'
            if r['content'] == None: r['content'] = 'Unknown'
            if r['source']['id'] == None: r['source']['id'] = 'Unknown'
        return render(req,'index.html', {'res': searchRes, 'cou': countries.items()})

def getCategory(req, ct):
    searchRes = {}
    catNews = requests.get('https://newsapi.org/v2/top-headlines?country=in&pageSize=100&category='+ct+'&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    searchRes = json.loads(catNews.content)
    for r in searchRes['articles']:
        if r['author'] == None: r['author'] = 'Unknown'
        if r['urlToImage'] == None: r['urlToImage'] = 'Unknown'
        if r['description'] == None: r['description'] = 'Unknown'
        if r['content'] == None: r['content'] = 'Unknown'
        if r['source']['id'] == None: r['source']['id'] = 'Unknown'
    return render(req,'index.html', {'res': searchRes, 'cou': countries.items()})

def getCountry(req, cid):
    searchRes = {}
    countriesNews = requests.get('https://newsapi.org/v2/top-headlines?country='+cid+'&pageSize=100&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    print(cid)
    searchRes = json.loads(countriesNews.content)
    for r in searchRes['articles']:
        if r['author'] == None: r['author'] = 'Unknown'
        if r['urlToImage'] == None: r['urlToImage'] = 'Unknown'
        if r['description'] == None: r['description'] = 'Unknown'
        if r['content'] == None: r['content'] = 'Unknown'
        if r['source']['id'] == None: r['source']['id'] = 'Unknown'
    return render(req,'index.html', {'res': searchRes, 'cou': countries.items()})