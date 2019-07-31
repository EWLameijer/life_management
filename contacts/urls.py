from django.urls import path

from . import views

urlpatterns = [
    path('persons/json', views.persons_to_json, name='persons_to_json'),
    path('persons/', views.persons, name='persons'),
    path('', views.contacts, name='contacts'),
]
