from django.urls import path, re_path
from Fuck import views

urlpatterns = [
    re_path(r'^about/contact/', views.contact),
    re_path(r'^about', views.about),
    path('', views.index),
]
