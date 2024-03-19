from django.db import models

# Create your models here.
class Notes(models.Model): 
    #inherit from models.Model - this way django knows that this is a model that will have an effect on the database. 
    # what attributes do you want in your database. 
    title = models.CharField(max_length = 200)
    text = models.TextField()
    created = models.DateTimeField(auto_now_add = True)
    