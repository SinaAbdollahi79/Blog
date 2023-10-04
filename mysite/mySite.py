from django.http import HttpResponse   

def mySiteView(request):
    return HttpResponse('<h1>this my firsr write on my own site </h1>')
