from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from .views import sendNotify

from django.conf import settings


class City(models.Model):

    cityAvailable = models.CharField(verbose_name="City", max_length=55)
    
    class Meta():
        verbose_name = "City available"

# Create your models here.
class Kennel(models.Model):
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    email = models.EmailField(verbose_name="Email", unique=True)
    username = models.CharField(verbose_name="Username", max_length=100, unique=True)
    city = models.CharField(verbose_name="City", max_length=55)
    address = models.CharField(verbose_name="address", max_length=55)
    cap = models.IntegerField(verbose_name="cap address", blank=True, null=True) 
    checked  = models.BooleanField(verbose_name="Kennel checked")
    piva = models.CharField(verbose_name="P.IVA", max_length=55, blank=True, null=True)
    pushat = models.DateField(auto_created=True, auto_now_add=True)
    
    def __str__(self):
        return self.username +" "+ self.city

  
    def addCityAvailable(obj):
       
        try:

            if not(City.objects.filter(cityAvailable = obj.city).exists()):
                cityAvailable = City()
               
                cityAvailable.cityAvailable =  str(obj.city).capitalize()
                cityAvailable.save()

                # send notify
                sendNotify("New city available", obj.city) 
        except Exception as e:  
            print(e)

    def removeCityAvaible(obj):
        try:
           
            if len(Kennel.objects.filter(city =  obj.city )) == 1:
             
               City.objects.filter(cityAvailable =  obj.city ).delete()
        except Exception as e:  
            print(e)

    def newUser(request, username, password):
       
        addUser = ""

        if request.user.is_authenticated:
            addUser = User.objects.filter(id = request.user.id)
            return addUser[0]
           
        else:
            # if user exist sistem declined and send to page login
            if User.objects.filter(username = username).exists():
                raise ValueError("User selection exist, go to login")
               
            try:   
              
                addUser = User.objects.create_user(username, username,  password )

            except Exception as e:
                raise ValueError("Sistem error")
                

            return addUser   


      # when use this method use try and exept
    # this fuction is used for add new kennel and return a array with first column is if query crushed and second is object
    def newKennel(request, addUser,addCity, addAddress, addPiva, addCap):
        try:
            
            if Kennel.objects.filter(email = addUser.email).exists():     
                raise ValueError("This user exist")
                

            kennel = Kennel()            
            kennel.user = addUser
            kennel.email = addUser.email
            kennel.username = addUser.username
            kennel.city = addCity.capitalize()
            kennel.address = addAddress
            kennel.piva = addPiva
            kennel.checked = False
            if addCap:
                kennel.cap = addCap
            
            kennel.save()
            
            newKennel = Kennel.objects.filter(email = addUser.email, username = addUser.username)

            sendNotify("New Kennel available","email: " + addUser.email+ '\ncity:' + addCity + ", " + addAddress +"\nlink: " + settings.LINK_URL[0] +"it/admin/authentication/kennel/" +str(newKennel[0].id)+   "/change") 

            # user authentication
            # login(addUser.username, addUser.password)
            Kennel.addCityAvailable(kennel)
        except Exception as e:
            raise ValueError("Sistem error")
    
   

    class Meta():
        verbose_name = "kennel"
        verbose_name_plural = "Kennels"



class SetNotification(models.Model):

    active = models.BooleanField(verbose_name="disattiva")

    class Meta():
        verbose_name = "Notifiche gestionale"


