from django.urls import path
from .views import livres

app_name = 'livres'

urlpatterns = [
    path('', livres),
]