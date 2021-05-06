from django.shortcuts import render
import requests
import json
# Create your views here.

def index(req):
    newsApi = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=291fabaef53b4aa48a118f8235a1ba3c')
    res = json.loads(newsApi.content)
    return render(req, 'index.html', {'res': res})