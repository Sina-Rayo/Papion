from rest_framework import serializers
from .models import Account ,Recepie ,Categorie


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
        fields = '__all__'
