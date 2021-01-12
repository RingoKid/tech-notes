from django.shortcuts import render
from .forms import AddNoteForm

def add_note(request):
    if request.method == 'POST':
        form = AddNoteForm(request.POST)
        if form.is_valid():
            form_data = form.save(commit=False)
            form_data.owner = request.user
            form_data.save()
            print(request.user)
    else:
        form = AddNoteForm()

    return render(request, 'add_note.html', {'form':form})