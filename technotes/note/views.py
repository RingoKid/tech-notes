from django.shortcuts import render, redirect
from .forms import UserRegistrationForm
from .models import User
from django.views.generic import View

from django.template.loader import get_template
from django.contrib.sites.shortcuts import get_current_site
from django.contrib import messages
from django.core.mail import send_mail 
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_text, DjangoUnicodeDecodeError
from .utils import token_generator
import threading


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            form.save()

            email = form.cleaned_data.get('email')
            user = User.objects.get(email=email)

            # Deactivate the account until verified
            user.is_active = False
            user.save()

            uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
            token = token_generator.make_token(user)

            domain = get_current_site(request).domain
            link = reverse('activate', kwargs={'uidb64':uidb64, 'token':token})

            htmly = get_template('Email.html')

            user_info = { 'username': user.first_name+user.last_name, 'token': 'http://'+domain+link }
            subject = 'Welcome to Tech Notes'

            html_content = htmly.render(user_info)

            email = EmailMessage(subject, html_content, to=[email])

            EmailThread(email).start()
            messages.success(request, 
                            f'A verification link was sent to your email address.',
                            'alert alert-success')

            
    else:
        form = UserRegistrationForm()
        
    return render(request, 'register.html', {'form':form})

class VerificationView(View):
    def get(self, request, uidb64, token):

        try:
            id = force_text(urlsafe_base64_decode(uidb64))
            user = User.objects.get(pk=id)

            if user.is_active:
                return redirect('login')
            user.is_active = True
            user.save()

        except Exception as e:
            pass

        return redirect('register')



class EmailThread(threading.Thread):

    def __init__(self, email_message):
        self.email_message = email_message
        threading.Thread.__init__(self)

    def run(self):
        self.email_message.send()