from django.http import HttpResponse
from django.shortcuts import render

# from .models import Tablon
from src.apps.posts.models import Post


def tablon_vista(request, simbolo):
    match simbolo:
        case "v":
            post_data = Post.objects.filter(tablon=1)
            context = {"post_data": post_data}
            return render(request, "tablon/videojuegos.html", context)
        case "i":
            return HttpResponse("Todavía en desarrollo, vuelva más tarde")
        case "a":
            return HttpResponse("Todavía en desarrollo, vuelva más tarde")
        case "tp":
            return HttpResponse("Todavía en desarrollo, vuelva más tarde")
        case "b":
            return HttpResponse("Todavía en desarrollo, vuelva más tarde")
        case _:
            return HttpResponse("404")
