
from django.http import HttpResponse
from django.shortcuts import render

# Une vue est une fonction qui accepte un objet HttpRequest comme paramètre et retourne un objetHttpResponse  .

def hello(request):
    return HttpResponse("<h1>hello Django!</h1>")

def about(request):
    return HttpResponse("<h1>information</h1>")
