from django.http import HttpResponse
from django.shortcuts import render


def tablon_vista(request, simbolo):
    match simbolo:
        case "v":
            return render(request, "tablon/videojuegos.html")
        case _:
            return HttpResponse("404")
