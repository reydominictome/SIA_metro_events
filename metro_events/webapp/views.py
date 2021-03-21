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

class MetroEventsHomeView(View):
    def get(self, request):
        return render(request, 'webapp/Home.html')        

