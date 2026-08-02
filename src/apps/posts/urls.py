from django.urls import include, path

from . import views

urlpatterns = [
    # path("post/"),
    path("post/nuevo/", views.posting_view, name="posting_view"),
    path("post/nuevo/form", views.posting_form, name="posting_form"),
    # path("post/eliminar/<int:id>"),
]
