from django.shortcuts import render, redirect
from .forms import AddNoteForm
from django.views.generic import ListView, DetailView, DeleteView
from .models import Note

def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.owner = request.user
            form_data.save()

            return redirect('note_list')
    else:
        form = AddNoteForm()

    return render(request, 'add_note.html', {'form':form})

class NoteList(ListView):
    context_object_name = 'notes'
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteDetail(DetailView):
    model = Note

class NoteDelete(DeleteView):
    model = Note

    success_url ="/technotes/list/"