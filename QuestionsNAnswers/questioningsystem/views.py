# Create your views here.
from django.shortcuts import render

def fbLogin(request):
    context = {}
    return render(request, 'login.html', context)