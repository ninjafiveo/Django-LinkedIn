#This is pre configured file.
from django.shortcuts import render
# Add the following
from django.http import HttpResponse
from datetime import datetime
# from django.contrib.auth.decorators import login_required
# Add below for the class based views.
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context = {'today':datetime.today()} #! taken from the def home function. Commented out the code below.
    
class AuthorizedView(LoginRequiredMixin ,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'
    
# Create your views here.
#! def home(request):
    # return HttpResponse("Hello, Ninjas!") # Use this to return just an HttpResonse to the page. 
    # After a you create a template (home/templates/home/welcome.html) you'll want to 'render' it. 
    # return render(request, 'home/welcome.html', {}) 
    
    #! commented out next line for Class-Based views section above.
    # return render(request, 'home/welcome.html', {'today':datetime.today()}) #Passing through a value into the welcome.html template. 

def about(request):
    return HttpResponse("An about us page could go here. This is just a test. ")

#@login_required #<-- This is a decorator. Added this and the page is only accessible if logged in. If user is not logged in the page is blocked. 

#@login_required(login_url='/admin')# this modifies the code above to redirect to the admin page so the user doesn't get a 404 page. You can create a new template and tell the user to "Click here to login" or whatever. 
# def authorized(request):
#     return render(request, 'home/authorized.html', {})