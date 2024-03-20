from django.shortcuts import render
from .models import Notes #Import the models(tables from the database. We are going to use this to in our view.)
from django.http import Http404
from django.views.generic import DetailView, ListView

class NotesListView(ListView):
    model = Notes
    context_object_name = "notes" # this is our whole end point. Now we just need to change our end point url. 
    template_name = "notes/notes_list.html"

class NotesDetailView(DetailView):# Takes care of complexity of errors
    model = Notes
    context_object_name = "note"
    template_name = "notes/notes_details.html"

# old endpoint. No longer needed since we added class NotesListView(ListView)
#def list(request): # Create a function to receive request. 
    #all_notes = Notes.objects.all() #A Variable that calls all the notes in our Database. ? If the note database is mammoth, is it smart to do this way?
    #return render(request, 'notes/notes_list.html', {'notes':all_notes}) #render the view with a template we'll create later.

# This is the same as what we did earlier, except we are querying for all notes and sending them to the template.

### Might need to uncomment if errors occur. 
# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note does not exist.")
#     return render(request, 'notes/notes_details.html', {'note':note})
