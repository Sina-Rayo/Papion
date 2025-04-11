from django.shortcuts import render
from .models import Account , Recepie , Categorie
from .serializer import AccountSerializer , RecepieSerializer , CategorieSerializer

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view


@api_view()
def main_page(request:Request):
    object_categorie_list = CategorieSerializer(Categorie.objects.all() , many=True)
    # categorie_list = []
    # for item in object_categorie_list:
    #     categorie_list.append(CategorieSerializer(item).data)

    recepie_list = RecepieSerializer(Recepie.objects.order_by("likes")[:10] , many=True)
    top_users = AccountSerializer(Account.objects.order_by("been_liked")[:5] , many=True)
    return Response({'categories':object_categorie_list.data , 'recepies':recepie_list.data , 'users':top_users.data} , status.HTTP_200_OK)
    # return render(request , 'sth.html' , {categories:categorie_list , recepies:recepie_list , users:top_users})

@api_view()
def categorie_page(request:Request , cat):
    recepie_list = RecepieSerializer(Recepie.objects.filter(categorie__name =cat).order_by("likes") , many=True)
    return Response({'recepies':recepie_list.data} , status.HTTP_200_OK)
    # return render(request , "sth.html" , {recepies : recepie_list})

@api_view()
def recepie_page(request:Request ,slug):
    recepie = RecepieSerializer(Recepie.objects.get(slug=slug))
    return Response({'res':recepie.data} , status.HTTP_200_OK)
    # return render(request , "sth.html" , {res : recepie})


def signup(request):
    user = User.objects.create_user("john", "lennon@thebeatles.com", "johnpassword") # -> Saves user itself
    user.last_name = "Lennon"
    user.set_password("new password")
    user.save()


def login(request):
    user = authenticate(username="john", password="secret")
    if user is not None:
        # A backend authenticated the credentials
        pass
    else:
        # No backend authenticated the credentials
        pass

def account(request):
    pass

def create_recepie(request):
    pass

def what_to_cook(request):
    pass

def search(request):
    pass
