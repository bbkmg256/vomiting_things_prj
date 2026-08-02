from django.http import HttpResponse
from django.shortcuts import redirect, render


# Vista del template para postear
def posting_view(request):
    return render(request, "posts/post.html")


# NOTA:
# - El redireccionamiento acá tiene que ser condicionado para que redirija al post publicado
# Vista para el formulario para postear
def posting_form(request):
    if request.method == "POST":
        print(f"{request.POST['post']}")
        # Redireciona a la vista del post
        return redirect("posting_view")
    return HttpResponse("Mal :(")
