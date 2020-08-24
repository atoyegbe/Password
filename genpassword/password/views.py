from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout 
from .forms import UserForm 

from .utils import generate_password
# Create your views here.
def home(request):
    
    if request.is_ajax():
        password = generate_password()
        
        return JsonResponse({'password': password}, status=200)
        
    return render(request, 'main.html')


def passwordsView(request):

	return render(request, 'passwords.html', context={})


def registerView(request):

    form = UserForm
    return render(request, 'Register.html', context={'form': form})



def loginView(request):

	return render(request, 'login.html', context={})

def logoutView(request):
	pass 
