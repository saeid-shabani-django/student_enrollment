from django.urls import path
from . import views

urlpatterns = [
     path('',views.student),
     path('new_registration/',views.registration,name='newregistration'),
     path('registered/',views.registered ,name='registered'),
     path('search/',views.search ,name='search'),
     
]
