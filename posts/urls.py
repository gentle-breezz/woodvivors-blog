'''
Qui gli url che i visitatori possono richiedere vengono mappati con delle
funzioni all'interno di views.py che servono i template HTML
'''
from django.conf.urls import url
from django.contrib import admin
from . import views

app_name = 'posts'

urlpatterns = [
    url(r'^$', views.post_list, name="lista_post"),
    url(r'^create/$', views.post_create, name="crea"),
    url(r'^(?P<slug>[\w-]+)/$', views.post_detail, name="post_singolo"),
]
