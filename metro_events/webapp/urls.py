from django.urls import path, include
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'webapp'

urlpatterns = [
    path('index', views.MetroEventsIndexView.as_view(), name='metro_event_view'),
]