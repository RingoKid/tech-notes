from django.urls import path
from django.conf.urls import url, include

from .views import add_note, NoteList, NoteDetail, NoteDelete

urlpatterns = [
    path('add_note/', add_note, name='add_note'),
    path('list/', NoteList.as_view(), name='note_list'),
    path('<pk>/', NoteDetail.as_view(), name='note_detail'),
    path('<pk>/delete/', NoteDelete.as_view(), name='note_delete'),
]