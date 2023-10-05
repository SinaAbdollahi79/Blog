from django.shortcuts import render
from django.http import HttpResponse   

def home(request):
    return render(request, 'index.html')

def about(request):
    return HttpResponse('<h1>sina abdollahi  </h1>')

def contact(request):
    return HttpResponse('<h1>0913*****44 </h1>')

