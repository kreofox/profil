from django.urls import path
from django.views.generic import TemplateView
from Fuk import views

urlpattens = [
    path('', views.index),
    path(r'^mainthing', views.mainthing),
    path("Profil\ ", TemplateView.as_view(template_name="about.html", extra_context = {"header": "Profil"})),
    path("contact\ ", TemplateView.as_view(template_name="contact.htmml")),
    path("set", views.set),
    path("get", views.get),
    
    ]
