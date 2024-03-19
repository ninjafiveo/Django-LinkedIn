from django.contrib import admin

#import
from . import models

# Register your models here.
class NotesAdmin(admin.ModelAdmin): #inherits from admin.ModelAdmin
    #pass
    list_display = ('title',) #add so the display of the note is = to the title rather than "Notes Object 1"... also remember for tuple, you need need to add the "," comma after it, or it is not a tuple.

admin.site.register(models.Notes, NotesAdmin)
#now you'll be able to see the notes in the Admin Panel.
#While we'll write code to add it, but for now you can manually add a note. 