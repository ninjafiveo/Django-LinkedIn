"""
URL configuration for smartproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include #added include when creating urls.py in the home app. Include function will be used to pass the file to the url patterns as a string.

#import files here from views.py so we have access to the function we created. 
# from home import views # Getting rid of this when we create the urls.py in the the home app.

urlpatterns = [
    path('admin/', admin.site.urls),
    #add path to the views file in home app.
    # path('home/', views.home), # got rid of these when creating the urls.py in the home app.
    # path('about/', views.about),# got rid of these when creating the urls.py in the home app.
    #note: if you have multiple paths with the same name, home/, django loads the first and never looks at the second. Could lead to potential errors. 
    
    # New after creating the urls.py file in home app.
    path('', include('home.urls')),
    
    #added from notes app
    path('smart/', include('notes.urls')), #all the urls added in the notes app will be after "smart/". This is to help keep the project organized. 
    
]
