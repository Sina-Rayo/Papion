from django.shortcuts import render
from models import Account , Recepie , Categorie

from django.contrib.auth.models import User
from django.contrib.auth import authenticate


def main_page(request):
    categorie_list = Categorie.objects.all()
    recepie_list = Recepie.objects.order_by("likes")[:10].get()
    top_users = Account.objects.order_by("been_liked")[:5].get()
    # Send to client

def categorie_page(request , cat):
    recepie_list = Recepie.objects.filter(categorie__name =cat).order_by("likes")
    # Send to client

def recepie_page(request , slug):
    recepie = Recepie.objects.get(slug=slug)
    # Send to client

###############################

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
