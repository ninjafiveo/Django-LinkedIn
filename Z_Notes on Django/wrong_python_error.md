Below is the conversation with ChatGPT that started because from when code base was downloaded to another computer, from github and it wouldn't run. 

I downloaded a Django project from Github. I am attempting to run in it a virtual environment. I go the virtual environment running (named virtuoso) but now  i am getting an error that says: 

(virtuoso) PS C:\Users\mcctc\Documents\GitHub\Django-LinkedIn> python manage.py runserver
No Python at '"/Library/Frameworks/Python.framework/Versions/3.11/bin\python.exe'
(virtuoso) PS C:\Users\mcctc\Documents\GitHub\Django-LinkedIn>

How do I fix this?
ChatGPT
The error message you're encountering suggests that the Django project you're trying to run is configured to use a specific Python interpreter located at "/Library/Frameworks/Python.framework/Versions/3.11/bin\python.exe", which is a path that typically would be found on a macOS system rather than Windows. However, since you're running this on a Windows machine (as indicated by the C:\Users\... path), this is likely causing the issue.

To fix this, you'll need to ensure that the Django project is using the Python interpreter from your virtuoso virtual environment. Here are some steps to resolve this:

Activate Virtual Environment:
Ensure that your virtual environment virtuoso is activated. You've mentioned it's running, but just to reiterate, you can activate it by navigating to your project directory in the terminal and running:

shell
Copy code
.\virtuoso\Scripts\activate
You should see the (virtuoso) prefix in your terminal indicating the virtual environment is active.

Check Python Path in Your Virtual Environment:
Once the virtual environment is activated, check the Python executable path to ensure it's pointing to the Python interpreter within your virtual environment:

shell
Copy code
which python   # On Unix/Linux/macOS
# or
Get-Command python   # On Windows PowerShell
This should point to a path inside your virtuoso directory.

Reconfigure the Project's Interpreter (if applicable):

If you're using an IDE like PyCharm or VSCode, ensure the project's Python interpreter is set to the one in your virtuoso virtual environment.
If there's a configuration file in the Django project specifying the Python interpreter (not common, but possible in some setups), update it to the correct path.
Install Project Requirements:
Ensure all the project's dependencies are installed within the virtual environment by running:

shell
Copy code
pip install -r requirements.txt
Make sure you're in the project directory where requirements.txt is located.

Run Django Server:
Try running the Django development server again with:

shell
Copy code
python manage.py runserver
If you're still facing issues, the problem might be more specific to your project's configuration or the virtual environment setup. In that case, reviewing the project's documentation for any setup instructions specific to Windows or reaching out to the project's maintainers for advice might be beneficial.

User
Ok. This is the python I have after running the Get-Command:

(virtuoso) PS C:\Users\mcctc\Documents\GitHub\Django-LinkedIn> Get-Command python

CommandType     Name                                               Version    Source
-----------     ----                                               -------    ------
Application     python.exe                                         3.10.11... C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Scripts\python.exe

It looks like `it's a different version. How do I fix this to get the code to run?
ChatGPT
Given that the Python version in your virtual environment is different from the one expected by the Django project (which appears to be looking for Python 3.11 based on the error message), there are a few approaches you can take to resolve this:

1. Upgrade Python in the Virtual Environment
If the Django project specifically requires Python 3.11 due to certain features or dependencies, you might need to upgrade the Python version in your virtual environment to Python 3.11. However, this typically means creating a new virtual environment with Python 3.11, since changing the Python version directly in an existing virtual environment can lead to complications.

First, ensure you have Python 3.11 installed on your system. If not, download it from the official Python website and install it. Then, create a new virtual environment using Python 3.11:

powershell
Copy code
# Navigate to your project directory if you aren't already there
cd C:\Users\mcctc\Documents\GitHub\Django-LinkedIn

# Deactivate the current virtual environment
deactivate

# Remove the old virtual environment (optional, but keeps things clean)
rm -r virtuoso

# Create a new virtual environment with Python 3.11
python3.11 -m venv virtuoso

# Activate the new virtual environment
.\virtuoso\Scripts\activate

# Install the required dependencies
pip install -r requirements.txt
2. Adjust the Django Project to Work with Python 3.10
If upgrading to Python 3.11 is not viable for some reason (e.g., Python 3.11 is not compatible with other dependencies you have), you can check if the Django project can run under Python 3.10. This would involve:

Checking the requirements.txt or any other dependency files to ensure all packages are compatible with Python 3.10.
Testing the Django project functionalities in a development setting to ensure everything works as expected under Python 3.10.
3. Check for Hardcoded Python Paths
The error message you initially encountered (No Python at '"/Library/Frameworks/Python.framework/Versions/3.11/bin\python.exe") suggests there might be a hardcoded path to a Python executable. This is unusual for Django projects but can happen in some configurations or custom scripts.

Search the project files for the hardcoded path ("/Library/Frameworks/Python.framework/Versions/3.11/bin\python.exe") and replace it with a relative path to Python that leverages the virtual environment (usually just python or python3).
Check for any environment variables or configurations in IDE settings that might be pointing to the specific Python path and adjust them accordingly.
Moving Forward
After making these adjustments, try running the Django server again with python manage.py runserver. If you encounter any Django or Python errors, they will likely be more specific to the project's code or dependencies, and you can address them based on the error messages provided.

User
When I tried to install python 3.11, I got the following error:
PS C:\Users\mcctc\Documents\GitHub\Django-LinkedIn> python3.11 -m venv virtuoso
python3.11 : The term 'python3.11' is not recognized as the name of a cmdlet, function, script file, or operable program. Check the spelling of the name, or if a path 
was included, verify that the path is correct and try again.
At line:1 char:1
+ python3.11 -m venv virtuoso
+ ~~~~~~~~~~
    + CategoryInfo          : ObjectNotFound: (python3.11:String) [], CommandNotFoundException
    + FullyQualifiedErrorId : CommandNotFoundException
ChatGPT
The error message you're seeing when trying to create a virtual environment with Python 3.11 (python3.11 : The term 'python3.11' is not recognized...) suggests that Python 3.11 isn't installed or isn't recognized by that specific name in your system's PATH.

Here are a few steps you can take to resolve this:

1. Verify Python 3.11 Installation
First, ensure Python 3.11 is indeed installed on your system. You can check this by running:

shell
Copy code
python --version
# or
py --version
If Python 3.11 is installed, one of these commands should return a version number that starts with 3.11. If it's not installed, you'll need to download and install it from the official Python website.

2. Check for Multiple Python Versions
If you have multiple versions of Python installed, Windows might not recognize python3.11 as a valid command. Instead, you can use the py launcher (which is installed with Python on Windows) to specify the version. First, check what versions are available:

shell
Copy code
py -0
This will list all the Python versions recognized by the py launcher.

3. Create a Virtual Environment with the Specific Version
If Python 3.11 is installed and listed by the py launcher, you can then create a virtual environment using that specific version by specifying the version with the py command:

shell
Copy code
py -3.11 -m venv virtuoso
This tells the py launcher to use Python 3.11 to create the virtual environment named virtuoso.

4. Activate the Virtual Environment
Once the virtual environment is created, activate it with:

shell
Copy code
.\virtuoso\Scripts\activate
You should see the (virtuoso) prefix in your terminal, indicating that the virtual environment is active.

5. Install Dependencies
Ensure you install all required dependencies within the virtual environment:

shell
Copy code
pip install -r requirements.txt
This assumes you have a requirements.txt file in your project directory listing all necessary packages.

Additional Note
If you continue to have issues or Python 3.11 is not available, you might consider using the version of Python you already have installed (3.10.11, as per your previous message) unless the project specifically requires Python 3.11. In many cases, Python projects are backward compatible within the same major version number (e.g., Python 3.10 and 3.11).

User
Seems like all is setup and working. But now I am getting an error when I execute: python manage.py runserver

(virtuoso) PS C:\Users\mcctc\Documents\GitHub\Django-LinkedIn> python manage.py runserver 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 26, 2024 - 09:37:00
Django version 5.0.3, using settings 'smartproject.settings'
Starting development server at http://127.0.0.1:8000/       
Quit the server with CTRL-BREAK.

Not Found: /
[26/Mar/2024 09:37:03] "GET / HTTP/1.1" 404 2634


Keep in mind it the program was running fine on my other computer. 
ChatGPT
The message you're seeing indicates that the Django development server is running correctly, but when it receives a request for the root URL (/), it's unable to find a corresponding view or URL pattern, resulting in a 404 Not Found error. This isn't necessarily an error with Django or your environment setup; it might simply mean that the root URL hasn't been defined in your project's URL configurations.

Here are a few steps to diagnose and potentially resolve this issue:

1. Check urls.py
Ensure your project's urls.py (typically found in the project's main application directory) includes a URL pattern for the root path ('/'). It might look something like this:

python
Copy code
from django.urls import path
from . import views  # Import your views module

urlpatterns = [
    path('', views.home, name='home'),  # Ensure there's a pattern for the root URL
]
In this example, views.home refers to a view function named home in your views.py file that should render a response for the root URL.

2. Verify the View Exists
Make sure the view referenced by your root URL pattern (e.g., views.home in the example above) actually exists in your views.py file and is capable of returning an HTTP response.

python
Copy code
from django.http import HttpResponse

def home(request):
    return HttpResponse("Hello, world. You're at the home page.")
3. Check for Application Inclusion in INSTALLED_APPS
If your URL patterns are defined within an application inside your project, ensure that this application is included in the INSTALLED_APPS setting in your project's settings.py file. This might look like:

python
Copy code
INSTALLED_APPS = [
    ...
    'your_app_name',
    ...
]
4. Application URLs Included in Project URLs
If your URLs are defined in an application's urls.py, ensure that these URLs are included in your project's main urls.py file using include(). For example:

python
Copy code
from django.urls import path, include  # Import include

urlpatterns = [
    path('', include('your_app_name.urls')),  # Include your app's URLs
]
5. Clear Browser Cache or Try a Different Endpoint
Sometimes browsers cache responses, leading to misleading outcomes. Try clearing your browser's cache or accessing a different endpoint that you know exists, such as /admin/.

6. Differences Between Environments
Since you mentioned the project was running fine on another computer, consider any environmental differences. These could include different settings in settings.py (for development vs. production), database configurations, or installed apps. Make sure your current environment matches the necessary configurations that were in place on the other computer.

If after these steps you're still encountering issues, it might be helpful to review the project's documentation or any setup instructions to ensure all configurations are correctly ported to your current environment.

User
The project folder is "smartproject" below is the code from urls.py in that folder:

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

App 1 is "notes" 
Here is the code from urls.py in that folder: 
from django.urls import path
from . import views

urlpatterns = [
    # path('notes', views.list),
    path('notes/', views.NotesListView.as_view(), name="notes.list"),
    path('notes/<int:pk>', views.NotesDetailView.as_view(), name="notes.detail"),
]
# next you need to add this file exists in the smartnote project folder so traffic can be redirected here. 


App 2 is "home", below is the code from urls.py in that file: 
# Created this file to make sure things are more organized and modular.
from django.urls import path
from . import views

#add same patterns from urls.py in the project folder smartnotes
urlpatterns = [
    # path('home/', views.home),
    path('home/', views.HomeView.as_view()),
    path('about/', views.about),
    # path('authorized/', views.authorized),
    path('authorized/', views.AuthorizedView.as_view()),
]

Also, if it matters, here is the code from settings.py in the "smartproject" folder:
"""
Django settings for smartproject project.

Generated by 'django-admin startproject' using Django 5.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-dvsz!%_f)fblrypf))&ar*7c-ldlq#36)r3j953*1c_^&eds10'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    
    #apps
    'home', # This needed added so Django knew there was another app installed. The LinkedIn tutorial did not mention that.
    'notes', #app added to test working with databases 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'smartproject.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'static/templates'
            ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                
            ],
        },
    },
]

WSGI_APPLICATION = 'smartproject.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = [ 
    BASE_DIR / 'static'
]

# Default primary key field type
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


What do I need to do to fix that error?
ChatGPT
Given the code snippets and the structure you've provided, it seems like everything is set up correctly for your Django project. The 404 Not Found error for the root URL (/) might simply be due to the lack of a specific view or template to handle requests to the root URL.

However, you've included a path in your main urls.py within the smartproject directory that directs the root URL to your home application:

python
Copy code
path('', include('home.urls')),
And within your home application's urls.py, you've defined a route that seems like it should handle the root URL:

python
Copy code
path('home/', views.HomeView.as_view()),
Given this setup, visiting http://127.0.0.1:8000/home/ should work and display whatever HomeView.as_view() is set to display. If you want http://127.0.0.1:8000/ (the root URL) to display what's currently being displayed at /home/, you'll need to adjust the path in your home application's urls.py to handle the root URL:

python
Copy code
path('', views.HomeView.as_view()),  # This will now handle the root URL
If this adjustment doesn't resolve the issue, or if the root URL should display something else, you might need to add a new view and URL pattern specifically for handling the root URL. For example, you could add the following view in your home/views.py:

python
Copy code
from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'index.html'
And then update your home/urls.py to include this view:

python
Copy code
path('', views.IndexView.as_view()),
Ensure that you have an index.html template in your templates directory that this view will render.

Lastly, double-check that your templates directory is correctly set up and recognized by Django. According to your settings.py, it looks for templates in BASE_DIR / 'static/templates'. Make sure your templates (like index.html) are located in that directory, and the directory structure is as expected.

User
That didn't seem to help. Here is more info that might help in the debugging:

When I try to go to http://127.0.0.1:8000/admin/ i get the following error in the browser: A server error occurred.  Please contact the administrator.

And in the terminal the following errors show: 
(virtuoso) PS C:\Users\mcctc\Documents\GitHub\Django-LinkedIn> python manage.py runserver 
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
March 26, 2024 - 09:48:45
Django version 5.0.3, using settings 'smartproject.settings'
Starting development server at http://127.0.0.1:8000/       
Quit the server with CTRL-BREAK.

[26/Mar/2024 09:48:52] "GET /admin/ HTTP/1.1" 302 0
Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\base.py", line 220, in _get_response
    response = response.render()
               ^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\response.py", line 114, in render
    self.content = self.rendered_content
                   ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\response.py", line 92, in 
rendered_content
    return template.render(context, self._request)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\backends\django.py", line 
61, in render
    return self.template.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\loader_tags.py", line 159, in render
    return compiled_parent._render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\loader_tags.py", line 159, in render
    return compiled_parent._render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\defaulttags.py", line 396, in render
    tzinfo = timezone.get_current_timezone() if settings.USE_TZ else None
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 55, in inner
    response = get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\deprecation.py", line 134, in __call__
    response = response or self.get_response(request)
                           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 12, in load_tzdata
    return resources.files(package_name).joinpath(resource_name).open("rb")
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 22, in files        
    return from_package(get_package(package))
                        ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 53, in get_package  
    resolved = resolve(package)
               ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\resources\_common.py", line 44, in resolve      
    return cand if isinstance(cand, types.ModuleType) else importlib.import_module(cand)
                                                           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\importlib\__init__.py", line 126, in import_module        
    return _bootstrap._gcd_import(name[level:], package, level)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1126, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "<frozen importlib._bootstrap>", line 1204, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1176, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1140, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'tzdata'

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\wsgiref\handlers.py", line 137, in run
    self.result = application(self.environ, self.start_response)
                  ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\contrib\staticfiles\handlers.py", line 80, in __call__
    return self.application(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\wsgi.py", line 124, in __call__
    response = self.get_response(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\base.py", line 140, in get_response
    response = self._middleware_chain(request)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 57, in inner
    response = response_for_exception(request, exc)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 140, in response_for_exception
    response = handle_uncaught_exception(
               ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\core\handlers\exception.py", line 181, in handle_uncaught_exception
    return debug.technical_500_response(request, *exc_info)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 69, in technical_500_response
    html = reporter.get_traceback_html()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\views\debug.py", line 429, in get_traceback_html
    return t.render(c)
           ^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 171, in render
    return self._render(context)
           ^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 163, in _render
    return self.nodelist.render(context)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in render
    return SafeString("".join([node.render_annotated(context) for node in self]))
                              ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1000, in <listcomp>
    return SafeString("".join([node.render_annotated(context) for node in self]))
                               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 961, in render_annotated
    return self.render(context)
           ^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 1059, in render
    output = self.filter_expression.resolve(context)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\template\base.py", line 733, in resolve
    obj = template_localtime(obj, context.use_tz)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 161, in template_localtime
    return localtime(value) if should_convert else value
           ^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 180, in localtime
    timezone = get_current_timezone()
               ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 66, in get_current_timezone
    return getattr(_active, "value", get_default_timezone())
                                     ^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\Documents\GitHub\Django-LinkedIn\virtuoso\Lib\site-packages\django\utils\timezone.py", line 52, in get_default_timezone
    return zoneinfo.ZoneInfo(settings.TIME_ZONE)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "C:\Users\mcctc\AppData\Local\Programs\Python\Python311\Lib\zoneinfo\_common.py", line 24, in load_tzdata
    raise ZoneInfoNotFoundError(f"No time zone found with key {key}")
zoneinfo._common.ZoneInfoNotFoundError: 'No time zone found with key UTC'
[26/Mar/2024 09:48:53] "GET /admin/login/?next=/admin/ HTTP/1.1" 500 59


Can you fix this?
ChatGPT
The error messages you're seeing are related to a ZoneInfoNotFoundError exception being raised due to the inability to find the 'UTC' time zone information. This is likely because the tzdata package, which provides time zone data for the standard library's zoneinfo module, is either not installed or not accessible in your Python environment.

Here are the steps to resolve this issue:

1. Ensure tzdata is Installed
First, you should ensure that the tzdata package is installed in your virtual environment. You can do this by activating your virtual environment and running:

shell
Copy code
pip install tzdata
2. Verify Installation
After installing tzdata, you can verify that it's installed correctly by running:

shell
Copy code
pip list
This command will list all the packages installed in your virtual environment. Ensure that tzdata is in the list.

3. Run the Development Server Again
Once tzdata is installed, try running the Django development server again:

shell
Copy code
python manage.py runserver
Additional Steps
If the issue persists even after ensuring tzdata is installed, consider the following additional steps:

Check Python and Django Compatibility: Ensure that your Python version is compatible with the Django version you're using. Since you're using Django 5.0.3, it should be compatible with Python 3.11, but it's always good to double-check the Django release notes for any specific compatibility notes.

Update Django: If you're not using the latest patch version of Django 5.0.x, consider updating Django to the latest version within the same minor version series (e.g., from 5.0.3 to the latest 5.0.x version) to ensure you have all the latest fixes:

shell
Copy code
pip install --upgrade 'Django~=5.0.0'
Check for Environment-Specific Issues: Since you mentioned that the project was working fine on another computer, there might be some environment-specific issues at play. Ensure that all environment variables and any other configuration specific to your project are correctly set up on your current machine.

Review Project Settings: Take a close look at your settings.py, especially at the TIME_ZONE setting, to ensure it's correctly set to 'UTC' or any other desired time zone.

Following these steps should help resolve the issue related to the ZoneInfoNotFoundError and allow you to access the Django admin and other parts of your project without encountering the 500 server error.

