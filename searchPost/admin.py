from django.contrib import admin
from . import models as db
from authentication.models import Kennel
from django.utils.html import format_html
from django.conf import settings
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "size" , "category", "kannel", "go_to_kannel"]
    search_fields =  ["kannel__email", "category", "title"]
    list_filter = ["size", "pushat"]

    def go_to_kannel(self,obj):
           return format_html("<button><a href='"+ settings.LINK_URL[0]+"it/admin/authentication/kennel/{0}'/change/ target='_blank'>Kennel</a></button>", obj.id )

    

    def save_model(self, request,obj, form, change):
        Kennel.addCityAvailable(obj)

        db.Post.addNewCategory(obj)
        return super().save_model(request, obj, form, change)
    
    def delete_model(self, request, obj):
        Kennel.removeCityAvaible(obj)
        db.Post.removeCategory(obj)
        return super().delete_model(request, obj)
    

admin.site.register(db.Post, PostAdmin)
admin.site.register(db.Categoryes)
admin.site.register(db.Sizes)

