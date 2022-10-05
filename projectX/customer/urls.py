from django.urls import path
from . import views

app_name = "customer"

urlpatterns = [
    path('index', views.index, name="index"),
    path('add/', views.add, name="add"),
    path('register/', views.register, name="register"), 
    path("loginCustomer", views.loginCustomer, name="login"),
    path("logoutCustomer", views.logoutCustomer, name="logout"),
    path('sercives', views.service, name='services'),
    path('', views.home, name='home'),
    path('form', views.form, name='form'),
    path('join', views.join, name="join"),
    path('profile/<int:id>', views.profile, name='profile'),
    path('employees', views.list, name='list'),
    path("garden", views.garden, name="garden"),
    path("house", views.house, name="house"),
    path("roof", views.roof, name="roof"), 
    path("pipe", views.pipe, name="pipe")
]