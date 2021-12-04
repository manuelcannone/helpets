from django.core.checks import messages
from django.shortcuts import redirect, render
from . import models as db
from django.http import HttpResponse
from django.core.mail import send_mail
from django.template import loader
# Create your views here.

def home(request):
    result = render(request, "home.html")
    return result

def sendEmail(request, id):
    
    response = "L`email e` stata inviata corettamente"
    try:
        obj = db.Email.objects.filter(id = id)
        templateEmail = loader.render_to_string(
            "email/email.html",{
            "email" : obj[0].sender,
            "date" : obj[0].pushat,
            "message" : obj[0].message
         } )	
       
    except:
        response = "Errore invio email"
    
    
    return  HttpResponse(response)
	

def emailPreviews(request, id):
    try:
        obj = db.Email.objects.filter(id = id)
      
    except:
    
        redirect("")

    
    result = render(request, "email/emailPreview.html",  {
            "email" : obj[0].sender,
            "date" : obj[0].pushat,
            "message" : obj[0].message
         } )
    return result