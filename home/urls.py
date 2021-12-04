from django.urls import  path
from . import views as template

urlpatterns = [
    path("", template.home ,  name="home"),
    path("email/previews/<int:id>", template.emailPreviews)
]