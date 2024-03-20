from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes/', views.NotesListView.as_view()),
    path('notes/<int:pk>', views.NotesDetailView.as_view()),
]
# next you need to add this file exists in the smartnote project folder so traffic can be redirected here. 

