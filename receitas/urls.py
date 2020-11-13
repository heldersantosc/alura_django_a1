from django.urls import path

from . import views

# rota do app receita exibindo o index
urlpatterns = [
    path('', views.index, name="index")
]
