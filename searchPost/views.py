from django.http import response
from django.shortcuts import render, redirect
from django.db.models import Q
from authentication.admin import cityAdmin

from . import models as db
# Create your views here.
def search(request):
   
    posts = db.Post.objects.all()
    
    if request.method == "POST":
        cityPOST = request.POST.get("city", False)
        categoryPOST =  request.POST.get("category", False)
        sizePOST = request.POST.get("size", False )

        # print(cityPOST, categoryPOST, sizePOST)
        # if cityPOST != "" or categoryPOST != "" or sizePOST != "":
        #     posts = db.Post.objects.filter( city = "")
        #if cityPOST or categoryPOST or sizePOST: 

       
            
        if cityPOST:
            posts = db.Post.objects.filter( city = cityPOST)      
            
        if categoryPOST: 
            if not(cityPOST):
                posts =  db.Post.objects.filter( category__name = categoryPOST)
            posts.union(db.Post.objects.filter( category__name = categoryPOST))     
            
        if sizePOST:        
            posts.union(db.Post.objects.filter( size__name = sizePOST))     
            if not(cityPOST) and  not(categoryPOST):
                 posts =  db.Post.objects.filter( size__name = sizePOST)
      
        posts.distinct()
        
    response = render(request, "search.html", {
        "posts" : posts, 
        # "small" : small,
        # "medium" : medium,        # "big" : big,
    })
    return response


def searchSingle(request, id):
    try:
       
        post = db.Post.objects.filter(id = id)
        
        

    except Exception as e:
        # error ridirect
        redirect("")
 
    response = render(request, "singlePost.html", {
        "post" : post[0]
    })
    return response

