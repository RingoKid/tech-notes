from django.urls import path
from django.conf.urls import url, include

from .views import register, VerificationView

urlpatterns = [
    path('register/', register, name='register'),
    path('activate/<uidb64>/<token>',VerificationView.as_view(), name='activate'),

]