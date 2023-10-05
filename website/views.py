from django.shortcuts import render
from django.http import HttpResponse   

def home(request):
    return HttpResponse('<h1>this my firsr write on my own site & this is a homee page </h1>')

def about(request):
    return HttpResponse('<h1>sina abdollahi  </h1>')

def contact(request):
    return HttpResponse('<h1>0913*****44 </h1>')

