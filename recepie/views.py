from django.shortcuts import render
from .models import Account , Recepie , Categorie , Comment , Ingredient
from .serializer import AccountSerializer , RecepieSerializer , CategorieSerializer ,IngredientSerializer , CommentSerializer

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
# @authentication_classes([BasicAuthentication])
# @permission_classes([IsAuthenticated])
def main_page(request:Request):
    object_categorie_list = CategorieSerializer(Categorie.objects.all() , many=True)

    recepie_list = RecepieSerializer(Recepie.objects.order_by("likes")[:10] , many=True)
    top_users = AccountSerializer(Account.objects.order_by("been_liked")[:5] , many=True)
    return Response({'categories':object_categorie_list.data , 'recepies':recepie_list.data , 'users':top_users.data} , status.HTTP_200_OK)
    # return render(request , 'sth.html' , {categories:categorie_list , recepies:recepie_list , users:top_users})

@api_view(['GET'])
def categorie_page(request:Request , cat):
    recepie_list = RecepieSerializer(Recepie.objects.filter(categorie__name =cat).order_by("likes") , many=True)
    return Response({'recepies':recepie_list.data} , status.HTTP_200_OK)
    # return render(request , "sth.html" , {recepies : recepie_list})

@api_view(['GET' , 'POST'])
def recepie_page(request:Request ,slug):
    recepie = RecepieSerializer(Recepie.objects.get(slug=slug))
    ingredients = IngredientSerializer(Ingredient.objects.filter(recepie__slug=slug) , many=True)
    comments = CommentSerializer(Comment.objects.filter(recepie__slug=slug) , many=True)
    return Response({'res':recepie.data , 'comments':comments.data , 'ingredients':ingredients.data} , status.HTTP_200_OK)
    # return render(request , "sth.html" , {res : recepie})

def account(request):
    pass

@api_view(['POST'])
def create_recepie(request:Request):
    serializer = RecepieSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        text = serializer.validated_data['text']
        ac  = serializer.validated_data['account']
        # account = Account.objects.get(pk=ac)
        main_recepie = serializer.validated_data['main_recepie']
        # time = models.TimeField(null=True)
        # likes = models.IntegerField()
        # comments = models.ForeignKey(Comment , on_delete=models.CASCADE) 
        # date = models.DateTimeField(null=True)
        # img = serializer.validated_data['img']
        slug = name.replace(" ", "")
        cat  = serializer.validated_data['categorie']
        # categorie = Categorie.objects.get(pk=cat)
        print(ac.username)
        res = Recepie(name=name , text=text , account=ac , main_recepie=main_recepie , slug=slug , categorie=cat , likes=0)
        res.save()
        ing_list  = serializer.validated_data['ing_list'] # [[n , m , num] , [n , m , num]]
        for i in range(0,len(ing_list)):
            ing_name = ing_list[i][0]
            measurement = ing_list[i][1]
            number = ing_list[i][2]
            ing1 = Ingredient(name=ing_name , measurement=measurement , number=number , recepie=res)
            ing1.save()

    return Response({'Recepie has been made Successfully'}, status=200)


def what_to_cook(request):
    pass

def search(request):
    pass


# { "name" : "res1" ,
# "text" : " new text " ,
# "account" : 1 ,
# "main_recepie" : " main recepie " ,
# "categorie" : 1,
# "ing_list" : [["salt" , "pinch" , 2] , ["rice" , "cup" , 1]] 
# }