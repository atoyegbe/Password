from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages 
from .forms import UserForm 
from .models import Passwords
from django.shortcuts import render, redirect

from .utils import generate_password
# Create your views here.
def home(request):

    if request.is_ajax():
        password = generate_password()
        return JsonResponse({'password': password}, status=200)
    if request.method == 'POST':
        passwordname = request.POST["passwordname"]
        passwordsafe = request.POST["passwordsafe"]
        
        Passwords.objects.create(name=passwordname, password=passwordsafe)
        messages.success(request, 'Passwords saved!!')
    return render(request, 'main.html')



@login_required
def passwordsView(request):
    passwords = Passwords.objects.all()
    return render(request, 'passwords.html', context={'passwords': passwords})


def registerView(request):
    form = UserForm()
    if request.method == 'POST':
    	form = UserForm(request.POST)
    	if form.is_valid():
    		form.save() 
    		return redirect('login')
    		messages.success(request, "Account was created succesfully")
    	else:
    		form = UserForm()

    return render(request, 'Register.html', context={'form': form})



def loginView(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)

			return redirect('home')
			messages.success(request, 'Logged In succesfully')
		else:
			messages.error(request, "Please provide a valid info")


	return render(request, 'login.html', context={})

@login_required
def logoutView(request):
	logout(request)

	return redirect('home')
