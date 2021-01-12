from django.urls import path
from django.conf.urls import url, include

from .views import add_note

urlpatterns = [
    path('add_note/', add_note, name='add_note'),
]