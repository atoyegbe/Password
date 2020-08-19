from django.shortcuts import render
from django.http import JsonResponse

from .utils import generate_password
# Create your views here.
def home(request):
    
    if request.is_ajax():
        password = generate_password()
        
        return JsonResponse({'password': password}, status=200)
        
    return render(request, 'main.html')