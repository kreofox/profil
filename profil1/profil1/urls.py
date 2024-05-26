from django.urls import path
from profil import views

urlpatterns = [
    path("index", views.http),
    path("set", views.set),
    
]