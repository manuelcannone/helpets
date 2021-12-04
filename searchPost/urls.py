from django.urls import  path
from . import views as template

urlpatterns = [
    path("", template.search ,  name="search"),
    path("post/<int:id>", template.searchSingle, name="searchSingle")
]