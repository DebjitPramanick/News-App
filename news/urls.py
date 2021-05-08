from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('query/', views.query, name="query"),
    path('<str:ct>', views.getCategory, name="getCategory"),
    path('country/<str:cid>', views.getCountry, name="getCountry"),
]