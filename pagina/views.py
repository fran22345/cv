from django.shortcuts import render, redirect
from .models import *
from .forms import *
from  django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def primera (request):
    if request.method == "POST":
        name = request.POST.get("name") 
        messages = request.POST.get("message")+" "+ request.POST.get("contact_email")
        send_mail(name , messages, settings.EMAIL_HOST_USER,["borgesfrancisco162@gmail.com"],)
    return render(request, 'index.html')
