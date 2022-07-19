from django.http import Http404, HttpResponse
from django.shortcuts import render

# tohle je jen náhrada za databázi
# až budeme používat databáze, tahle data tu nebudou
slovnik = {
    "pes": "Pes štěká.",
    "kočka": "Kočka má devět životů.",
    "chameleon": "Chameleon umí měnit barvu.",
    "tučňák": "Tučňák má rád zimu.",
    "šimpanz": "Šimpanz jí banány.",
    "slon": "Slon je velký.",
    "žirafa": "Žirafa má dlouhý krk.",
    "krtek": "Krtek žije pod zemí."
}

# Create your views here.

# tomuhle se říká view funkce
def index(request):
    return render(request, "informace/index.html")

def slon(request):
    context = {
        "jmeno": "Jumbo",
        "barva": "modrou",
        "je_velky": False
    }
    return render(request, "informace/slon.html", context)

def zirafa(request):
    return render(request, "informace/zirafa.html", {
        "jmeno": "Amálka",
        "jídlo": "špenát",
        "vek": 7,
        "veta": "ahoj jak se máš",
        "slovo": "orangutan",
        "pocet_orangutanu": 5,
        "cislo": 56,
        "cislo_jako_string": "56",
        "pravda": True,
        "lez": False,
        "seznam_slov": ["jablko", "hruška", "pomeranč"]
    })

def seznam_zvirat(request):
    return render(request, "informace/seznam.html", {
        "seznam": slovnik
    })

def detail_zvirete(request, zvire):
    try:
        info = slovnik[zvire]
    except:
        raise Http404("Stránka neexistuje")
    return render(request, "informace/detail.html", {
        "zvire": zvire,
        "popis": info
    })
