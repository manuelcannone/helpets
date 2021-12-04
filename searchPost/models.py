from django.db import models
from django.utils import tree
from authentication.models import Kennel
from authentication.views import sendNotify
from django.contrib.auth.models import User

class Sizes(models.Model):

    name =  models.CharField(max_length=15)        
    def __str__(self):
        return self.name

class Categoryes(models.Model):

    name =  models.CharField(max_length=25) 

    def __str__(self):
        return self.name 
# Create your models here.


class Post(models.Model):

    kannel = models.ForeignKey(Kennel, on_delete=models.CASCADE)
    
    title = models.CharField(max_length=25)
    description = models.TextField(max_length=200, blank=True, null=True)
    size =  models.ForeignKey(Sizes, on_delete=models.SET_NULL,blank=True, null=True )
    category = models.ForeignKey(Categoryes, on_delete=models.SET_NULL,blank=True, null=True )
    city = models.CharField(verbose_name="City", max_length=30)
    img1 = models.ImageField(upload_to='post', blank=True, null=True )
    img2 = models.ImageField(upload_to='post', blank=True, null=True )
    img3 = models.ImageField(upload_to='post', blank=True, null=True )
    img4 = models.ImageField(upload_to='post', blank=True, null=True)
    numberOfSaved = models.IntegerField()
    pushat = models.DateField(auto_created=True, auto_now_add=True)   
    
    def addNewCategory(obj):    
       
        try:
            if not(Categoryes.objects.filter(name = obj.category).exists()):
                categoryes = Categoryes()
                categoryes.name = obj.category = str(obj.category).capitalize()
                categoryes.save()
                sendNotify("New category available", obj.category) 
        except Exception as e:
            print(e)

    def removeCategory(obj):
        try:
            if len(Categoryes.objects.filter(category = obj.category)) == 1:
                Categoryes.objects.filter(name =obj.category).delete()
        except Exception as e:
            print(e)
        
    def newPost(self, kennel, title, description, size, category, img1,img2,img3,img4):
            pass
        
   
class SavePost(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL,blank=True, null=True )
    post = models.ForeignKey(Post, on_delete=models.SET_NULL,blank=True, null=True )
    order_date = models.DateField(null=True)
    
    # def addToSave(self, id, user):
        
    #     post = Post.objects.get(id= id)
        
    #     try:
    #         if SavePost.objects.filter(id = id, user = user):
    #             raise "this post is saved"
    #         else:
    #             SavePost.user = user
    #             SavePost.post = post
                
    #     except Exception as e:
    #         raise "error"
        
        
    