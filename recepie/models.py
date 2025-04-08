from django.db import models # type: ignore

class Account(models.Model):
    username = models.CharField(max_length=20)
    # recepies = models.ForeignKey(Recepie , on_delete=models.CASCADE) 
    # likes = models.ForeignKey(Recepie , on_delete=models.PROTECT)
    # comments = models.ForeignKey(Comment , on_delete=models.CASCADE)
    been_liked = models.IntegerField()

class Categorie(models.Model):
    name = models.CharField(max_length=20)
    # recepies = models.ForeignKey(Recepie , on_delete=models.PROTECT)

class Recepie(models.Model):
    name = models.CharField(max_length=25)
    text = models.TextField()
    account = models.ForeignKey(Account , on_delete=models.PROTECT)
    likers = models.ManyToManyField(Account)
    # ingredients = models.ForeignKey(Ingredient , on_delete=models.CASCADE) 
    main_recepie = models.TextField()
    time = models.TimeField()
    likes = models.IntegerField()
    # comments = models.ForeignKey(Comment , on_delete=models.CASCADE) 
    date = models.DateTimeField()
    img = models.ImageField()
    slug = models.SlugField()
    categorie = models.ForeignKey(Categorie , on_delete=models.CASCADE)

class Ingredient(models.Model):
    name = models.CharField(max_length=20)
    measurement = models.CharField(max_length=20)
    number = models.IntegerField()
    recepie = models.ForeignKey(Recepie , on_delete=models.PROTECT) 

class Comment(models.Model):
    text = models.TextField()
    recepie = models.ForeignKey(Recepie , on_delete=models.PROTECT) 
    account = models.ForeignKey(Account , on_delete=models.PROTECT) 
