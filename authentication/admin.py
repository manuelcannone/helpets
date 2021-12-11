from django.contrib import admin

from . import models as db
# Register your models here.
from django.utils.html import format_html


class KennelAdmin(admin.ModelAdmin):
    search_fields  = ["user__username", "email", "city" ]
    list_display  = ["username","email","city","piva","lastlogin", "checked"]
    list_filter  = ["checked"]

    def save_model(self, request,obj, form, change):
        db.Kennel.addCityAvailable(obj)
        return super().save_model(request, obj, form, change)

    def lastlogin(self,obj):
     
        try:
            return obj.User.last_login
        except Exception as e:
            
            return format_html("<b style='color: red;'>Error last login</b>")

    def delete_model(self, request, obj):
      
        db.Kennel.removeCityAvaible(obj)    
        return super().delete_model(request, obj)
    

class cityAdmin(admin.ModelAdmin):
    search_fields  = ["cityAvailable"]
    list_display  = ["cityAvailable","look_kennel_with_this_city"]
   
    def look_kennel_with_this_city(self, obj):
        return format_html("<button><a href='/it/admin/authentication/kennel/?q={0}' target='_blank'>LOOK</a></button>", obj.cityAvailable )


class SetNotificationAdmin(admin.ModelAdmin):
    list_display = ["active"]

    



admin.site.register(db.Kennel, KennelAdmin)
admin.site.register(db.City, cityAdmin)
admin.site.register(db.IsKennel)

admin.site.register(db.SetNotification,SetNotificationAdmin)