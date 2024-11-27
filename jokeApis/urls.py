from django.urls import path
from .views import fetch_jokes

urlpatterns = [
path('fetch-jokes/', fetch_jokes, name='fetch_jokes'),
]