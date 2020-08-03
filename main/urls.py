from django.urls import path,include
from . import views

app_name = 'main'

urlpatterns = [
    path('',views.indexview,name='index'),
    path('/about',views.aboutusview,name='about'),
    path('/contact',views.contactview,name='contact'),
    path('/auth',views.authview,name='authy'), 
]
