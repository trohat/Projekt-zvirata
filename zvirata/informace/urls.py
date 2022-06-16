from django.urls import path

from . import views

urlpatterns = [
    path("seznam/", views.seznam_zvirat),
    path("slon/", views.slon),
    path("zirafa/", views.zirafa),
    path("<zvire>/", views.detail_zvirete),
    path("", views.index)
]
