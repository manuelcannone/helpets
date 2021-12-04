from django.contrib import admin
from . import models as db
from django.utils.html import format_html
from django.conf import settings
class EmailAdmin(admin.ModelAdmin):

    list_display = ["sender", "username", "text","previews", "pushat"]
    search_fields = ["sender", "username"]
    
    def previews(self, obj):

       return format_html("<button><a href='"+ settings.LINK_URL[0]+"it/email/previews/{0}' target='_blank'>previews</a></button>", obj.id )

admin.site.register(db.Email, EmailAdmin)
