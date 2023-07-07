from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class NewsLetter (models.Model):
    email = models.EmailField(null=False)
    disable = models.BooleanField(null=False,default=False)

class Userr(models.Model):
    username = models.CharField(max_length=20,null=False,default="")
    userr = models.OneToOneField(User,on_delete=models.CASCADE,null=True)
    nom = models.CharField(max_length=10,null=False)
    prenom = models.CharField(max_length=10,null=False)
    email = models.EmailField(null=False)
    rh = models.BooleanField(null=False,default=False)
    traitementCV = models.BooleanField(null=False,default=False)

class Cv(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de creation")
    file = models.FileField(upload_to="file/", null=False)
    fileID = models.CharField(max_length =20 , null=False)


class SessionCV(models.Model):
    hashed_id = models.CharField(max_length=200,null=False,default="")
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de creation")
    etat = models.IntegerField(null=False,default=0)
    cvUploaded = models.BooleanField(null=False,default=False)
    accepted = models.BooleanField(null=False,default=False)
    usernameRh = models.CharField(max_length=20,null=False)
    usernameUser = models.CharField(max_length=20,null=False)

class Message(models.Model):
    date = models.DateTimeField(default=timezone.now, verbose_name="Date de d'envoi")
    contenu = models.CharField(max_length=1000,null=False,default="")
    type = models.CharField(max_length=10,null=False,default="text")
    cv = models.ManyToManyField("Cv",null=True)
    session = models.ManyToManyField("sessionCV",null=True)
    username = models.CharField(max_length=20, null=False)
    messageFromRh = models.BooleanField(default=False,null=False)


"""
class ContactUs (models.Model):
    email = models.EmailField(null=False)
    nom = models.CharField(null=False,max_length=20)
    """
