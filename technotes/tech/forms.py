from .models import Note
from django import forms
from .models import Note

class AddNoteForm(forms.ModelForm):
    title = forms.CharField(max_length=50)
    content = forms.CharField(widget=forms.Textarea)
    
    class Meta:
        model = Note
        fields = ['title', 'content']
    