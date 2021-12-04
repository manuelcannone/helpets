from django.urls import path
from . import views as template

urlpatterns = [
    path("register/", template.register, name="register")                      
]