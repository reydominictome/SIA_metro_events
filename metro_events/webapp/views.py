import math
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import View, TemplateView
from django.contrib import messages
from django.db.models import Q
from django.http import HttpResponse, Http404
from .forms import UserForm
from datetime import datetime
from webapp.models import User

# Create your views here.

class MetroEventsIndexView(View):
    def get(self, request):
        return render(request, 'webapp/Users.html')

    def post(self, request):
    	if request.method == 'POST':
    		form = UserForm(request.POST)
    		form.first = request.POST.get("first_name")
    		form.middle = request.POST.get("middle_name")
    		form.last = request.POST.get("last_name")
    		form.username = request.POST.get("username")
    		form.password = request.POST.get("password")
    		form.email = request.POST.get("email")
    		form.regdate = request.POST.get("register_date")
    		form.status = request.POST.get("status")

    		user = User.objects.all()
    		count = 0

    		for user in users:
    			if (user.email == form.email):
    				count = 1

    		if(count==0):
    			if(form.is_valid()):
    				firstname = request.POST.get("first_name")
    				middlename = request.POST.get("middle_name")
    				lastname = request.POST.get("last_name")
    				username = request.POST.get("username")
    				password = request.POST.get("password")
    				email = request.POST.get("email")

    				form = User(firstname = firstname, middlename = middlename, 
    							lastname = lastname, username=username, 
    							password=password, email=email)
    				form.save()

    				Mbox('Successfully Registered', 'Success', 64)
    				return redirect('webapp:metro_event_view')

    		else:
    			Mbox('Account already exist.', 'Error', 16)

    	return render(request, 'Home.html', {'form':form}))

class MetroEventsHomeView(View):
    def get(self, request):
        return render(request, 'webapp/Home.html')        

