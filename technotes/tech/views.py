from django.shortcuts import render, redirect
from .forms import AddNoteForm
from django.views.generic import ListView, DetailView, DeleteView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from .models import Note

@login_required()
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

class NoteList(LoginRequiredMixin, ListView):
    login_url = '/accounts/login/'
    context_object_name = 'notes'
    def get_queryset(self):
        return Note.objects.filter(owner=self.request.user)

class NoteDetail(LoginRequiredMixin, DetailView):
    login_url = '/accounts/login/'
    model = Note

class NoteDelete(DeleteView):
    model = Note

    success_url ="/technotes/list/"

class NoteUpdate(UpdateView):
    model = Note

    fields = [ 
        "title", 
        "content"
    ]

    success_url ="/technotes/list/"