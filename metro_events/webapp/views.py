import math
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404
from .forms import *
from datetime import datetime
from django.contrib.auth.hashers import make_password
from .models import *

# Create your views here.

class MetroEventsIndexView(View):
    def get(self, request):
        return render(request, 'webapp/Users.html')
    
    def post(self, request):
        if request.method == 'POST':
            if "btnRegister" in request.POST:
                form = RegistrationForm(request.POST)	
                data = request.POST

                if form.password == form.cpassword:
                    user = User.objects.all()
                    count = 0

                    for user in user:
                        if(user.email == form.email):
                            count = 1

                    if count == 0:
                        if form.is_valid():
                            password = data.get("password")
                            cpassword = data.get("cpassword")
                            username = data.get("username")
                            firstname = data.get("fname")
                            midname = data.get("mname")
                            lastname = data.get("lname")
                            email = data.get("email") 

                            form = User(first_name = firstname, middle_name = midname, last_name = lastname, 
                                    email = email, password = password)   
                            form.save()
                            form.password = make_password(form.password)
                            form.save()

                            messages.success(request, '<b>' + username + '</b> was registered successfully!')
                            return redirect('webapp:landing')

                    messages.success(request, '<b>' + email + '</b> is in use!')
                    return redirect('webapp:landing')

                messages.success(request, 'Please make sure that the passwords are the same')
                return redirect('webapp:landing')

            messages.success(request, 'Something went terribly wrong')
            return redirect('webapp:landing')
        else:
            messages.success(request, 'Something went terribly wrong')
            return redirect('webapp:landing')

class MetroEventsHomeView(View):
    def get(self, request):
        return render(request, 'webapp/Home.html')        

