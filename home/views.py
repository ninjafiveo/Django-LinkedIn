#This is pre configured file.
from django.shortcuts import render
# Add the following
from django.http import HttpResponse
from datetime import datetime

# Create your views here.
def home(request):
    # return HttpResponse("Hello, Ninjas!") # Use this to return just an HttpResonse to the page. 
    # After a you create a template (home/templates/home/welcome.html) you'll want to 'render' it. 
    # return render(request, 'home/welcome.html', {}) 
    return render(request, 'home/welcome.html', {'today':datetime.today()}) #Passing through a value into the welcome.html template. 



def about(request):
    return HttpResponse("An about us page could go here. This is just a test. ")
