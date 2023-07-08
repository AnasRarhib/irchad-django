from django import forms
from django.contrib.auth.models import User


class InscriptionForm(forms.Form):
    email = forms.EmailField(required=True,max_length=40,widget=forms.EmailInput(attrs={'name':'your_email','id':'your_email','class':'input-text','pattern':'[^@]+@[^@]+.[a-zA-Z]{2,6}'}))
    username = forms.CharField(required=True,max_length=20,widget=forms.TextInput(attrs={'name':'username','id':'username','class':'input-text'}))
    nom = forms.CharField(required=True,max_length=20,widget=forms.TextInput(attrs={'name':'nom','id':'nom','class':'input-text'}))
    prenom = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'name':'prenom','id':'prenom','class':'input-text'}))
    mdp = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(attrs={'name':'password','id':'password','class':'input-text'}))
    mdp2 = forms.CharField(required=True, max_length=20, widget=forms.PasswordInput(attrs={'name':'comfirm_password','id':'comfirm_password','class':'input-text'}))

class ConnectionForm(forms.Form):
    username = forms.CharField(required=True,max_length=20,widget=forms.TextInput(attrs={'name':'username','id':'username','class':'input-text'}))
    mdp = forms.CharField(required=True,max_length=20,widget=forms.PasswordInput(attrs={'name':'password','id':'password','class':'input-text'}))

class CreateSession(forms.Form):
    file = forms.FileField(required=True,widget=forms.FileInput(attrs={'id': 'fileupload', 'class': 'form-control'}))

"""
class ContactUs(forms.Form):
    message = forms.CharField(widget=forms.Textarea(attrs={'id':'message','class':'message','class':'input-forms'}))
    mail = forms.CharField(required=True,max_length=40,widget=forms.EmailField(attrs={'name':'mail','class':'input-form','id':'mail'}))
    objet = forms.CharField(required=True,max_length=55,widget=forms.TextInput('name':'objet','id':'objet','class':'input-form'))
""""
""""
class ContactUsForm(forms.Form):
    email = forms.EmailField(required=True,max_length=20,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'Votre Email *'}))
    nom = forms.CharField(required=True, max_length=20 ,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Votre Nom *'}))
    prenom = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Votre Prénom *'}))
    phone = forms.CharField(required=True, max_length=20, widget=forms.TextInput(attrs={'type':'tel','class':'form-control','placeholder':'Votre Numéro de Tel *'}))
    message = forms.CharField(required=True,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'Votre Message *'}))
    newsLetterConfirm = forms.BooleanField(required=True,widget=forms.CheckboxInput(attrs={'class':'form-control'}))

"""