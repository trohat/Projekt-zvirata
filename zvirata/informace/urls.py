from django.urls import path

from . import views

urlpatterns = [
    path("seznam/", views.seznam_zvirat, name="seznam"),
    path("slon/", views.slon, name="slon"),
    path("zirafa/", views.zirafa, name="zirafa"),
    path("detail/<zvire>/", views.detail_zvirete, name="detail"),
    path("", views.index, name="index")
]
