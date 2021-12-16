
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
                UserInformation = db.UserInformation()
                UserInformation.user = user 
                UserInformation.IsKennel = False
                if request.POST['city']:
                    UserInformation.city = str(request.POST['city']).capitalize()
                UserInformation.save()
                
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

def loginRoute(request):
    if request.method == 'POST':   
        username = request.POST["username"]
        password = request.POST['password1']
        user = authenticate(username=username, password=password)
        
        if user is not(None):
            login(request, user)
            messages.success(request, "Registrazione effettuata con successo")
            return redirect('/')
        
        else:
            # error not validate
            messages.error(request, "Email o password errati")
            storage = messages.get_messages(request)
            storage.used = True
            print("Error")
            return redirect('/auth/login/')        
            
            
    return render(request, "login.html", )        


def kennelLogin(request):
    if request.method == 'POST': 
    
        user = ""
        
        if request.user.is_authenticated:
            
            user = request.user

        else:
            username = request.POST["username"]
            password = request.POST['password1']
            userAuth = authenticate(username=username, password=password)  
            
            if User.objects.filter(username = username).exists():
            
                if userAuth is not(None):
                    # if user exist execute basic login
                    login(request, userAuth) 
                
                else:
                    # error not validate
                    messages.error(request, "Email o password errati")
                    storage = messages.get_messages(request)
                    storage.used = True
                    print("Error")
                    return redirect('/auth/loginKennel/')  
                
            else:
                # error not validate
                messages.error(request, "Utente inesistente")
                storage = messages.get_messages(request)
                storage.used = True
                print("Error")
                return redirect('/auth/register/') 
            
                
          
        try:
            print("dwqdwqd")
            address = False
            piva = False
            cap = False
            if request.POST["address"]:
                address = request.POST["address"]
                
            if  request.POST["iva"]:
                piva =  request.POST["iva"]
                
            if request.POST["cap"]:
                cap = request.POST["cap"]
            db.Kennel.newKennel(request, user, request.POST["city"], address, piva, cap)
            return redirect("/") 
                
        except Exception as e:
            messages.error(request, e)
            storage = messages.get_messages(request)
            storage.used = True
            print("Error")
            return redirect('/auth/register/') 
        
           
    return render(request, "registerKennel.html")