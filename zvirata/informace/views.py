from django.http import Http404, HttpResponse
from django.shortcuts import render

# tohle je jen náhrada za databázi
# až budeme používat databáze, tahle data tu nebudou
slovnik = {
    "pes": "Pes štěká.",
    "kočka": "Kočka má devět životů.",
    "chameleon": "Chameleon umí měnit barvu",
    "tučňák": "Tučňák má rád zimu.",
    "šimpanz": "Šimpanz jí banány.",
    "slon": "Slon je velký.",
    "žirafa": "Žirafa má dlouhý krk.",
    "krtek": "Krtek žije pod zemí."
}

# Create your views here.

# tomuhle se říká view funkce
def index(request):
    odpoved = "<h1>Tohle je obsah.</h1>"
    odpoved += "<p>Tohle je odpověď na požadavek, který byl poslán "
    odpoved += "pomocí metody "
    odpoved += request.method
    odpoved += ".</p>"
    odpoved += "<p>To sme chytrý, co? :) :) :) 🦉</p>"
    return HttpResponse(odpoved)

def slon(request):
    return HttpResponse("<p>Tohle je povídání o slonovi.</p>")

def zirafa(request):
    return HttpResponse("Tohle je zirafa. <p>Haf haf</p>")

def seznam_zvirat(request):
    response = "<h1>Tohle je seznam všech zvířat v naší aplikaci</h1>"
    response += "<ol>"
    for zvire, popis in slovnik.items():
        response += "<li>"
        response += f"<b>{zvire.capitalize()}</b>"
        response += f" - {popis}"
        response += "</li>"
    response += "</ol>"
    response += "<p>&copy; Moje aplikace."
    return HttpResponse(response)

def detail_zvirete(request, zvire):
    try:
        info = slovnik[zvire]
    except:
        raise Http404("Stránka neexistuje")
    response = f"<p>Hledáš informace o zvířeti {zvire}.</p>"
    response += f"<p>Tady jsou: {info}</p>"
    return HttpResponse(response)


