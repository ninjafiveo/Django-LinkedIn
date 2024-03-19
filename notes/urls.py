from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
]
# next you need to add this file exists in the smartnote project folder so traffic can be redirected here. 

