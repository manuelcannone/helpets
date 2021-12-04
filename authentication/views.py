from django.db.models.fields import EmailField
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from . import models as db
from . import forms
from pushbullet import Pushbullet

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
    if request.method == "POST":
        form = forms.NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("")
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            return redirect("")
	  
        
    response = render(request, "register.html")
    return response

# def logout(request):
#     logout(request)
#     # basic logout
#     messages.success("Il logout e` riuscito perfettamente")
#     redirect("")
