from django.urls import path
from . import web

urlpatterns = [
    path('',web.home,name='home'),
    path('count/',web.count,name='count'),
    path('about/',web.about,name='about'),
]
