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
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'

class IngredientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingredient
        fields = '__all__'

class RecepieCreateSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=25)
    text = serializers.CharField()
    account = serializers.IntegerField()
    # account = serializers.ForeignKey(Account , on_delete=models.PROTECT)
    # likers = serializers.ManyToManyField(Account , related_name='likes' , null=True)
    main_recepie = serializers.CharField()
    # time = serializers.TimeField(null=True)
    # likes = serializers.IntegerField()
    # date = serializers.DateTimeField(null=True)
    # img = serializers.ImageField()
    # slug = serializers.SlugField()
    categorie = serializers.IntegerField()
    ingiridients = serializers.ListField(child=serializers.DictField(child=serializers.CharField()))

class CreateCommentSerializer(serializers.Serializer):
    text = serializers.CharField()