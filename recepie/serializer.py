from rest_framework import serializers
from .models import Account ,Recepie ,Categorie ,Comment ,Ingredient


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = '__all__'

class CategorieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Categorie
        fields = '__all__'

class RecepieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Recepie
        fields = ( "name" ,"text" , "account" , "likers" , "main_recepie" , "categorie" , "account")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'