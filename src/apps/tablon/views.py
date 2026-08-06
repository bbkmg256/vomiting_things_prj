from django.http import HttpResponse
from django.shortcuts import render

# from .models import Tablon
from apps.posts.models import Post


def tablon_vista(request, simbolo):
    match simbolo:
        case "v":
            # Se ordena el queryset por fecha de publicación
            post_data = Post.objects.filter(tablon=1).order_by(
                # El - (guión) le dice a django que la organizacion será de forma descendente
                "-fecha_publicacion",
                "-hora_publicacion",
            )

            """
            Esta consulta trae los items realizando un filtrado y generando un campo especifico que agrupa el numero de objetos que tiene relacionado cada objeto del modelo especifo.
            """
            # post_data = (
            #     Post.objects.filter(tablon=1)
            #     .annotate(total_respuestas="comentario_set")
            #     .order_by(
            #         # El - (guión) le dice a django que la organizacion será de forma descendente
            #         "-fecha_publicacion",
            #         "-hora_publicacion",
            #     )
            # )

            # print(type(post_data))
            # print(len(post_data))
            # print(post_data.first().id)
            context = {"post_data": post_data, "simb": simbolo}
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
