from django.urls import include, path

from . import views

urlpatterns = [
    path("tablon/<str:simbolo>/", views.tablon_vista, name="tablon_vista"),
    # path("tablon/<str:simbolo>/post/<int:id>"),
    # path("tablon/<str:simbolo>/post/nuevo/"),
]
