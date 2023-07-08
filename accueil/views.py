from django.shortcuts import render
from .models import *
from .forms import *
#from password_strength import PasswordPolicy
from django.contrib.auth import logout,authenticate, login
from django.http import HttpResponse, JsonResponse
from django.contrib.auth.models import User
import random
import json
from django.core.serializers import serialize

def connect(request):
    if request.user.is_authenticated:
        return True
    return False

def getUserr(request):
    U_ID = request.user
    return Userr.objects.get(userr=U_ID)

def isRh(user):
    if user.rh :
        return True
    return False

def home(request):
    connected = connect(request)
    if connected:
        user = getUserr(request)
        is_rh = isRh(user)
    return render(request,"accueil/home.html",locals())

def inscription(request):
    connected = connect(request)
    if connected:
        return home(request)
    form = InscriptionForm(request.POST or None)
    if form.is_valid():
        print("form is good ")
        # COLLECTING DATA FROM FORM
        username = form.cleaned_data['username']
        email = form.cleaned_data['email']
        password = form.cleaned_data['mdp']
        nom = form.cleaned_data['nom']
        prenom = form.cleaned_data['prenom']
        password2 = form.cleaned_data['mdp2']
        # _________________TEST NOT EMPTY_______________________
        if username == None or email==None or password== None or nom== None or prenom==None or password2==None :
            empty_error = True
            print("yes is empty")
            return render(request, 'accueil/inscription.html', locals())
        # _________________USERNAME EXIST & LENGHT VERIFICATION_________________
        for i in User.objects.all():
            if i.username == username and len(password)>=5:
                username_exits = True
                return render(request,'accueil/inscription.html',locals())
        # _________________MAIL EXIST VERIFICATION_________________
        for i in Userr.objects.all():
            if i.email == email:
                email_exists = True
                return render(request, 'accueil/inscription.html', locals())
        # _________________PASSWORD STRENGHT VERIFICATION___________________
        """policy = PasswordPolicy.from_names(
            length=8,  # min length: 8
            uppercase=0,  # need min. 1 uppercase letters
            numbers=1,  # need min. 1 digits
            special=0,  # need min. 0 special characters
            nonletters=0,  # need min. 0 non-letter characters (digits, specials, anything)
        )
        test_password_strenght = policy.test(password)
        for t in test_password_strenght:
            password_strenght_error = True
            return render(request,'accueil/inscription.html',locals())"""
        # ________________TEST PASSWORD EQUAL_________________________
        if password != password2:
            password_equal_error = True
            return render(request, 'accueil/inscription.html', locals())
        # ________________TEST NOM LENGHT___________________________
        if len(nom)<=3:
            nom_lenght=True
            return render(request,"accueil/inscription.html",locals())
        # ________________TEST NOM LENGHT___________________________
        if len(prenom) <= 3:
            prenom_lenght=True
            return render(request, "accueil/inscription.html", locals())

        u = User.objects.create_user(username=username,password=password)
        u.save()
        userr = Userr(id=None,username=username,userr=u,nom=nom,prenom=prenom,email=email)
        userr.save()
        account_created=True
        return render(request,'accueil/inscription.html',locals())

    return render(request,'accueil/inscription.html',locals())

def seConnecter(request):
    connected = connect(request)
    if connected:
        return home(request)
    else:
        form = ConnectionForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['mdp']
            if password == None or username == None :
                return render(request,"accueil/seConnecter.html",locals())

            utilisateur = authenticate(username=username, password=password)
            if utilisateur:
                login(request, utilisateur)
                return home(request)
            else:
                error_connection = True

    return render(request,"accueil/seConnecter.html",locals())

def deconnection(request):
    logout(request)
    return home(request)

def irchad (request,session_id):
    session_id = int(session_id)
    connected = connect(request)
    if connected:
        user = getUserr(request)
        username = user.username
        is_rh = isRh(user)
        session_id = int(session_id)
        if session_id != 0:
            must_create_session = False
            if SessionCV.objects.filter(hashed_id=session_id).exists():
                session = SessionCV.objects.get(hashed_id = session_id)
                room = session.hashed_id
                if session.usernameUser != user.username :
                    return home(request)
            else:
                return home(request)
        else:
            must_create_session = False
            if SessionCV.objects.filter(usernameUser = user.username).exists():
                session = SessionCV.objects.get(usernameUser = user.username)
                session_id = session.hashed_id
                session_exist = True
                return render(request,"accueil/irchad.html",locals())
            else:
                must_create_session = True
                form = CreateSession(request.POST or None,request.FILES)
                if form.is_valid():
                    if form.cleaned_data['file'] == None:
                        return home(request)
                    else:
                        fileName = form.cleaned_data["file"].name
                        if fileName.endswith(".JPEG") or fileName.endswith(".PNG") or fileName.endswith(".jpg") or fileName.endswith('.pdf') or fileName.endswith('.word') or fileName.endswith(".png") or fileName.endswith(".JPG") or fileName.endswith(".PDF") or fileName.endswith(".WORD") or fileName.endswith(".jpeg"):
                            form_extension_valid = True

                            # __________verification if user got already a session__________
                            if SessionCV.objects.filter(usernameUser=user.username).exists():
                                alreadySession = True
                                session = SessionCV.objects.filter(usernameUser=user.username)[0]
                                session_id = session.hashed_id
                                session_exist = True
                                return render(request, "accueil/irchad.html", locals())

                            if Userr.objects.filter(rh=True).exists():
                                rh = random.choice(Userr.objects.filter(rh=True))
                                session = SessionCV(usernameUser=user.username, usernameRh=rh.username)
                                session.save()
                                cv = Cv(file=form.cleaned_data["file"])
                                cv.save()
                                cv.fileID = hash(cv.id)
                                cv.save()
                                message = Message(type="file",username=user.username,contenu="CV:"+fileName)
                                message.save()
                                message.session.add(session)
                                message.cv.add(cv)
                                session.hashed_id = hash(id)
                                if session.hashed_id <0:
                                    session.hashed_id = session.hashed_id * -1
                                session.save()
                                session_id = session.hashed_id
                                session_exist = True
                                return render(request, "accueil/irchad.html", locals())
                        else:
                            form_extension_valid = False
                            return render(request,"accueil/irchad.html",locals())
    else :
        return seConnecter(request)
    return render(request,"accueil/irchad.html",locals())

def getMessages(request,session_id):
    session = SessionCV.objects.get(hashed_id=session_id)
    messages = Message.objects.all()
    messages1 = []
    for m in messages :
        if m.session.all().count() > 0 :
            for s in m.session.all():
                if s.hashed_id == session_id:
                    messages1.append(m)

    serialized_data = serialize("json", messages1)
    serialized_data = json.loads(serialized_data)

    return JsonResponse({"messages":list(serialized_data)})

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    session_id = request.POST['session_id']
    session = SessionCV.objects.get(hashed_id=session_id)

    new_message = Message.objects.create(contenu=message, username=username,type="message")
    new_message.session.add(session)
    new_message.save()
    return HttpResponse('Message sent successfully')

############################################################################
######################## PARTIE RH #########################################
############################################################################

def listSessions(request):
    connected = connect(request)
    if connected:
        user = getUserr(request)
        username = user.username
        is_rh = isRh(user)
        if is_rh == True:
            return home(request)
        listSessionss = SessionCV.objects.all()
        return render(request,'accueil/rhListeSessions.html',locals())
    else:
        return home(request)

    return render(request,'accueil/rhListeSessions.html',locals())

def sessionRh(request,session_id):
    session_id = int(session_id)
    connected = connect(request)
    if connected:
        user = getUserr(request)
        username = user.username
        is_rh = isRh(user)
        if is_rh == True:
            return home(request)
        if SessionCV.objects.filter(hashed_id=session_id).exists():
            session = SessionCV.objects.get(hashed_id=session_id)
            usernameUser = session.usernameUser
            return render(request, "accueil/sessionRh.html", locals())
        else:
            return home(request)
    return render(request,"accueil/sessionRh.html",locals())

def sendRh(request):
    message = request.POST['message']
    username = request.POST['username']
    session_id = request.POST['session_id']
    session = SessionCV.objects.get(hashed_id=session_id)

    new_message = Message.objects.create(contenu=message, username=username,type="message",messageFromRh=True)
    new_message.session.add(session)
    new_message.save()
    return HttpResponse('Message sent successfully')