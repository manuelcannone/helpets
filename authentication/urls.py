from django.urls import path
from . import views as template

urlpatterns = [
    path("register/", template.register, name="register"),
    path("logout/", template.logoutRoute, name="logout" ),
    path("login/", template.loginRoute, name="login" ),      
    path("loginKennel/", template.kennelLogin, name="loginKennel" ),              
]