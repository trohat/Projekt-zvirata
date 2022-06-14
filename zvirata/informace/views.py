from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

# tomuhle se říká view funkce
def index(request):
    return HttpResponse("<h1>Tohle je obsah.</h1>")

def slon(request):
    return HttpResponse("<p>Tohle je povídání o slonovi.</p>")

def zirafa(request):
    return HttpResponse("Tohle je zirafa. <p>Haf haf</p>")
