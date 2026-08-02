from django.http import HttpResponse
from django.shortcuts import render

# from .models import Tablon
from src.apps.posts.models import Post


def tablon_vista(request, simbolo):
    match simbolo:
        case "v":
            # Se ordena el queryset por fecha de publicación
            post_data = Post.objects.filter(tablon=1).order_by(
                # El - (guión) le dice a django que la organizacion será de forma descendente
                "-fecha_publicacion",
                "-hora_publicacion",
            )
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
