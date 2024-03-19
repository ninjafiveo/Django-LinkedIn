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


####
Django Admin Interface 
Easy to create endpoints. 

The interface allows you to manipulate data and the admin interface comes built in.
http://127.0.0.1:8000/admin

Update Database migrations with: python manage.py migrate

Create a superuser - python manage.py createsuperuser
user: admin
email: michael.sekol@mahoningctc.com
password: password

imports in the views.py file:
from django.contrib.auth.decorators import login_required


#######
## Introduction to Django ORM
# ORM = Object Relational Mapping System. 
This handles database communication and changes.
### How to create your own models.
Django 
You have to create Class Models that will then be transformed by migrations into database tables. 
Each class, known as a model, is a database table and each class attribute is a column. 
The way we transform a model into a database table is by the creation of migrations.
Migrations will have the step-by-step transformation taht a database must to to apply the changes made in the code. 
The command "migrate" to apply changes made. 
We can also use the command "make-migration" to create migration space on the current code.
The process of using a class, defining a model, creating a migration, and appliying the migration and the changes to the database is the ORM's job. 

#### Creating a Model
Create a new app: django-admin startapp notes
notes being the name of the new app. 

Go to setting in smartproject project folder and add 'notes' to the apps. 

Go to models.py in notes folder to create the models to use in app.

* Sample Code Below
from django.db import models

# Create your models here.
class Notes(models.Model): 
    #inherit from models.Model - this way django knows that this is a model that will have an effect on the database. 
    # what attributes do you want in your database. 
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)

* Now Run
python manage.py makemigrations 

Once ran a new python file will be created in the notes/migrations folder. 

So far nothing has been changed in the database. We've just created a set of instructions. What we need to do now is apply the migrations to the database with:  python manage.py migrate   

The changes are applied to the database and now we have a new table. 

When creating a new model (table), you have to go into admin.py and add it. (Under the app folder. In this case "notes")


Django admin is highly configurable.

#### Using Django shell or creating and querying data
The Django Shell
You can run queries in the terminal.

* In the terminal: python manage.py shell
The python interpreter starts, but it is integrated with your app.
>>> from notes.models import Notes
>>> mynote = Notes.objects.get(pk='1')
>>> mynote.title
'My First Note'
>>> mynote.text
"Django and Ninja's are Awesome."
>>> Notes.objects.all()
<QuerySet [<Notes: Notes object (1)>]>
>>> new_note = Notes.objects.create(title="A note from the terminal", text="This is another note, but created in the terminal rather than the admin panel.")
>>> Notes.objects.all()
<QuerySet [<Notes: Notes object (1)>, <Notes: Notes object (2)>]>
Notes.objects.filter(title__startswith="A note")
<QuerySet [<Notes: Notes object (2)>]>
>>> Notes.objects.filter(text__icontains = 'Django')
<QuerySet [<Notes: Notes object (1)>]>
>>> Notes.objects.filter(text__icontains = 'Ninja')
<QuerySet [<Notes: Notes object (1)>]>
>>> Notes.objects.exclude(text__icontains = 'Django')
<QuerySet [<Notes: Notes object (2)>]>
>>> Notes.objects.filter(text__icontains = 'Django').exclude(title__icontains='Django')
<QuerySet [<Notes: Notes object (1)>]>
>>> Notes.objects.filter(text__icontains = 'is').exclude(title__icontains='Django')
<QuerySet [<Notes: Notes object (2)>]>

# Building Dynami Webpages.
## Creating a dynamic template.
Now that we have notes, we need to create a way to view them. So we're going to create a new way to view them. 

Go into views.py and create the following: 
from django.shortcuts import render
from .models import Notes #Import the models(tables from the database. We are going to use this to in our view.)

def list(request): # Create a function to receive request. 
    all_notes = Notes.objects.all() #A Variable that calls all the notes in our Database. ? If the note database is mammoth, is it smart to do this way?
    return render(request, 'notes/notes_list.html', {'notes':all_notes}) #render the view with a template we'll create later.

##### This is the same as what we did earlier, except we are querying for all notes and sending them to the template.

* Create a new urls.py file in the notes folder.
Add the following: 
from django.urls import path
from . import views

urlpatterns = [
    path('notes', views.list),
]
* next you need to add this file exists in the smartnote project folder so traffic can be redirected here. 


* In the urls.py folder in the smartproject project folder, we need to add the path to the notes app urls.py as well. (in the urlpatterns = [])

Add the following in the smartproject project folder:
    #added from notes app
    path('smart/', include('notes.urls')), #all the urls added in the notes app will be after "smart/". This is to help keep the project organized. 

### Time to add a new template to view the notes in the notes app folder.  
* Create a new folder in notes called 'templates' and then another folder inside there called 'notes'. (Again this might seem redundant but it's a good practice to keep the apps organized in the file structure.)
* Create a new file calles notes_list.html <- This should match file name from views.py

#### Display content of a single note.
Go to views and add a private key (pk)

def detail(request, pk):
    note = Notes.objects.get(pk=pk)
    return render(request, 'notes/notes_details.html', {'note':note})

* Next add the template.
notes_detail.html

* Need to add the url to urls.py in notes folder. But it will be different because we need to pass through the value of the note.
urlpatterns = [
    path('notes', views.list),
    path('notes/<int:pk>', views.detail),
] 
  
* Now you can pass through the value of a single note through the url. http://localhost:8000/smart/notes/2, http://localhost:8000/smart/notes/3, http://localhost:8000/smart/notes/"etc"
* There is a problem here though. If you pass through a value of a note that doesn't exist, an error will be thrown. (in debug mode you'll see the error. in production the user will just get a 500 internal server error)

To fix this, go back to the views.py file and add the following code: from django.http import Http404

Then add a try except statement in the detail function.
def detail(request, pk):
    try:
        note = Notes.objects.get(pk=pk)
    except Notes.DoesNotExist:
        raise Http404("Note does not exist.")
    return render(request, 'notes/notes_details.html', {'note':note})
* If you want you can add another template here for 404 errors.

### Class Based Views. 





