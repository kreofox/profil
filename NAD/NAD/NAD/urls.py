from django.urls import path, re_path
from Fuck import views

urlpatterns = [
    re_path(r'^about/contact/', views.contact, kwargs={"name":"Tom", "age":38}),
    re_path(r'^about', views.about),
    path('', views.index),
    path('https', views.https),
    path('set', views.set)
]
