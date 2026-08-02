from django.http import HttpResponse
from django.shortcuts import redirect, render


# Vista del template para postear
def posting_view(request, simbolo):
    context = {"simbolo": simbolo}
    return render(request, "posts/posting_form.html", context)


# NOTA:
# - El redireccionamiento acá tiene que ser condicionado para que redirija al post publicado
# Vista para el formulario para postear
def posting_form(request, simbolo):
    if request.method == "POST":
        # LOG para visualizar los post
        print(f"{request.POST['titulo_post']}\n{request.POST['contenido_post']}")
        # Redireciona a la vista del post
        match simbolo:
            case "v":
                return redirect("tablon_vista", simbolo)
            case _:
                return HttpResponse("404")
    return HttpResponse("Mal :(")
