Commands
Before you begin, you may need to install django. pip3 install django <- on mac, or just pip install django on pc

Start Ddjango Project: django-admin startproject name_of_project .

Note: the "." at the end is important. 

Create an app in the Django project:
django-admin startapp home
# home is could be named anything. Banana, fred, NameOfApp.

Run a new instance of the app/server
python manage.py runserver 

If you get a 404 error, as long as your Django file is in "debug" mode, a list of all the end points will appear. 
http://127.0.0.1:8000/ <- if this throws an error, it should give a list of the file paths available. Such as:
Page not found (404)
Request Method:	GET
Request URL:	http://127.0.0.1:8000/
Using the URLconf defined in smartproject.urls, Django tried these URL patterns, in this order:

1. admin/
2. home
The empty path didn’t match any of these.

You’re seeing this error because you have DEBUG = True in your Django settings file. Change that to False, and Django will display a standard 404 page.

###################
When I ran the app after we added the welcome.html template, and we had to render the template vs. send an HttpRequests, I got the error that the page could not be found. 

Solution: In the settings.py file, in the smartproject folder, I had to add the "home" app to:
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home', # This needed added so Django knew there was another app installed. The LinkedIn tutorial did not mention that. 
]

###############
Because of being able to pass through variables in python, this is the reason we don't use pure html in the html templates. We are actually using DTL (Django Template Language).

####
Good Software Projects should be well modularized. 
Each App should be self contained and everything that app needs is inside of it. 
You should be able to delete the entire app folder and everything else in the Django Project works prefectly. 





