from django.urls import path
from .views import *


urlpatterns = [
    path('',contact,name='contact'),
    path('con/',contactstring,name='con'),
    path('emprec/',empreco,name='emp'),
    path('sc/',sc,name='sc'),
]
