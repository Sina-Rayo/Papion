from django import forms

class User(forms.Form):
    user_name = forms.CharField(max_length=20)
    password = forms.CharField(max_length=30, widget=forms.PasswordInput)
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)
    email = forms.EmailField()

class Ingredient(forms.Form):
    name = name = forms.CharField(max_length=20)
    measurement = forms.CharField(max_length=20)
    number = forms.IntegerField()
    
class Recepie(forms.Form):
    name = forms.CharField(max_length=30)
    text = forms.forms.CharField(widget=forms.Textarea)
    # ingredients
    main_recepie = forms.forms.CharField(widget=forms.Textarea)
    time = forms.TimeField()
    img = forms.ImageField()
