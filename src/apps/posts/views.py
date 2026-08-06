from django.http import HttpResponse
from django.shortcuts import redirect, render

from apps.posts.models import Post
from apps.tablon.models import Tablon


# Vista del post
def post_view(request, simbolo, id_post):
    try:
        post = Post.objects.get(id=id_post)
        context = {"post": post, "simb": simbolo}
        return render(request, "posts/post.html", context)
    except Exception as e:
        print(f"{e}")
        return HttpResponse("404")


# Vista del template para postear
def posting_view(request, simbolo):
    context = {"simbolo": simbolo}
    return render(request, "posts/posting_form.html", context)


# NOTA:
# - El redireccionamiento acá tiene que ser condicionado para que redirija al post publicado
# Vista para el formulario para postear
def posting_form(request, simbolo):
    if request.method == "POST":
        # Hay que verificar que los campos no estén vacíos
        if not request.POST["titulo_post"].strip():
            print("LOG: Datos vacios")
            return redirect("tablon_vista", simbolo)
        # LOG para visualizar los post
        # print(f"{request.POST['titulo_post']}\n{request.POST['contenido_post']}")
        # Redireciona a la vista del post
        match simbolo:
            case "v":
                Nuevo_post = Post.objects.create(
                    titulo=request.POST["titulo_post"],
                    contenido=request.POST["contenido_post"],
                    tablon=Tablon.objects.get(id=1),
                )
                # No hace falta por que el metodo create ya lo persiste
                # Nuevo_post.save()
                return redirect("tablon_vista", simbolo)
            case _:
                return HttpResponse("404")
    return HttpResponse("Mal :(")
