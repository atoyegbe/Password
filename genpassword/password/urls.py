from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('passwords/', passwordsView, name='passwords'),


    path('register', registerView, name='register'),
    path('login', loginView, name='login'),
    path('logout', logoutView, name='logout'),
]
