'''
Definizioni delle funzioni che ritornano i template
'''
from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    # return HttpResponse('Questa è la HOMEPAGE')
    return render(request, 'homepage.html')

def about(request):
    # return HttpResponse('Questa è la pagina di about')
    return render(request, 'about.html')
