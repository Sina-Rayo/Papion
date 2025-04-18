from django.shortcuts import render
from .models import Account , Recepie , Categorie , Comment , Ingredient
from .serializer import AccountSerializer , RecepieSerializer , CategorieSerializer ,IngredientSerializer , CommentSerializer , RecepieCreateSerializer , CreateCommentSerializer

from rest_framework import status
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.decorators import api_view , authentication_classes , permission_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated

@api_view(['GET'])
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

@api_view(['GET' , 'POST' , 'PUT'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def recepie_page(request:Request ,slug):
    if request.method == 'POST': # for Comment
        serializer = CreateCommentSerializer(data=request.data)
        if serializer.is_valid():
            text = serializer.validated_data['text']
            recepie = Recepie.objects.get(slug=slug)
            ac = request.user.username
            account = Account.objects.get(username=ac)
            comment = Comment(text=text , account=account , recepie=recepie)
            comment.save()
            return Response({'Comment Created'}, status=200)
        return Response({'Error while sending Comment'}, status=200)
    elif request.method == 'PUT': #for likes
        recepie = Recepie.objects.get(slug=slug)
        ac = request.user.username
        account = Account.objects.get(username=ac)
        liker_list = recepie.likers.all()
        res_account = Account.objects.get(username=recepie.account.username)
        if account in liker_list:
            recepie.likes -= 1
            recepie.likers.remove(account)  
            res_account.been_liked -= 1 
            recepie.save() 
            res_account.save() 
            return Response({'Unliked'}, status=200)        
        else:
            recepie.likes += 1
            recepie.likers.add(account)
            res_account.been_liked += 1
            res_account.save()
            recepie.save()

        return Response({'liked'}, status=200)

    else:
        recepie = RecepieSerializer(Recepie.objects.get(slug=slug))
        ingredients = IngredientSerializer(Ingredient.objects.filter(recepie__slug=slug) , many=True)
        comments = CommentSerializer(Comment.objects.filter(recepie__slug=slug) , many=True)
        return Response({'res':recepie.data , 'comments':comments.data , 'ingredients':ingredients.data} , status.HTTP_200_OK)
        # return render(request , "sth.html" , {res : recepie})

def account(request):
    pass

@api_view(['POST'])
@authentication_classes([BasicAuthentication])
@permission_classes([IsAuthenticated])
def create_recepie(request:Request):

    serializer = RecepieCreateSerializer(data=request.data)
    if serializer.is_valid():
        name = serializer.validated_data['name']
        try:
            Recepie.objects.get(name=name)
            return Response({'Recepie already exists'}, status=200) 
        except:
            pass
        text = serializer.validated_data['text']
        # ac  = serializer.validated_data['account']
        # account = Account.objects.get(pk=int(ac))
        ac = request.user.username
        account = Account.objects.get(username=ac)
        main_recepie = serializer.validated_data['main_recepie']
        # time = models.TimeField(null=True)
        # likes = models.IntegerField()
        # comments = models.ForeignKey(Comment , on_delete=models.CASCADE) 
        # date = models.DateTimeField(null=True)
        # img = serializer.validated_data['img']
        slug = name.replace(" ", "")
        cat  = serializer.validated_data['categorie']
        categorie = Categorie.objects.get(pk=int(cat))
        res = Recepie(name=name , text=text , account=account , main_recepie=main_recepie , slug=slug , categorie=categorie , likes=0)
        res.save()

        ing_ser = serializer.validated_data['ingiridients']
        for i in range(0, len(ing_ser)):
            ing_name = ing_ser[i]["name"]
            measurement = ing_ser[i]["measurement"]
            number = ing_ser[i]["number"]
            ing1 = Ingredient(name=ing_name , measurement=measurement , number=number , recepie=res)
            ing1.save()  

        return Response({'Recepie has been made Successfully'}, status=200)
    return Response({'Not valid'}, status=200)


# {
# "name" : "res1" ,
# "text" : " new text " ,
# "account" : 1 ,
# "main_recepie" : " main recepie " ,
# "categorie" : 1

# ,
# "ingiridients": [{"name" : "salt" , "measurement":"pinch" , "number":"1"} , {"name" : "rice" , "measurement":"cup" , "number":"2"}]

# }