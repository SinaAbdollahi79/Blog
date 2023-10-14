from django.shortcuts import render
from django.http import HttpResponse   

def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    return render(request, 'contact.html')

