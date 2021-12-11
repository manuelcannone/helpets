
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from . import models as db
from . import forms
from pushbullet import Pushbullet
from validate_email import validate_email
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required

api_key = "o.IgYlz8u6K8YP6wZLyY9fRukLdaOv3Dqg"
PB = Pushbullet(api_key)


def sendNotify(title, body):

    try:
        setting = db.SetNotification.objects.filter()
        
        if setting[0].active == False:
            PB.push_note(title, body)

    except Exception as e:
        print(e)        

# # Create your views here.
def register(request):
    if request.method == 'POST':   
        form = UserCreationForm(request.POST)
     
        # add check of email
        emailCheck = validate_email(request.POST["username"])
        if emailCheck:
        
            if form.is_valid():
                form.save()
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password1')
                user = authenticate(username = username, password = password)
                login(request, user)
                
                # Create a variable to indicate if the user is a kennel
                user = User.objects.get(username = username)
                isKennel = db.IsKennel()
                isKennel.user = user 
                isKennel.IsKennel = False
                isKennel.save()
                messages.success(request, "Registrazione effettuata con successo")
                return redirect('/')
            else:
                #error not validate
                messages.error(request, "Qualcosa e` andato storto")
                storage = messages.get_messages(request)
                storage.used = True
                print("Error")
                return redirect('/auth/register/')
        else:
            
            messages.error(request, "Controlla la tua email")
            storage = messages.get_messages(request)
            storage.used = True
            
            print("Errore")
            return redirect('/auth/register/')

    return render(request, "register.html", )

@login_required
def logoutRoute(request):
    logout(request)
    messages.success(request, "Logout effettuato con sucesso")
    return redirect("/")

