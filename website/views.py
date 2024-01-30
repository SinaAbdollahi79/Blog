from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages
from django.conf import settings


def home(request):
    return render(request, 'website/index.html')

def about(request):
    return render(request, 'website/about.html')

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '.تیکت شما با موفقیعت ثبت شد')
        else:
            messages.error(request, '.متاسفانه تیکت شما ثبت نشد')
    google_maps_api_key = settings.GOOGLE_MAPS_API_KEY        
    form = ContactForm()

    return render(request, 'website/contact.html' , {'form': form ,'google_maps_api_key': google_maps_api_key})

