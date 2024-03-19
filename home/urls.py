# Created this file to make sure things are more organized and modular.
from django.urls import path
from . import views

#add same patterns from urls.py in the project folder smartnotes
urlpatterns = [
    path('home/', views.home),
    path('about/', views.about),
    path('authorized/', views.authorized),
    
]