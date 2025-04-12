from . import views
from django.urls import path

urlpatterns = [
    path('' , views.main_page),
    path('categories/<cat>' , views.categorie_page),
    path('recepie/<slug>' , views.recepie_page),
    path('create' , views.create_recepie),
]
