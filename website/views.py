from django.shortcuts import render
from website.forms import ContactForm
from django.contrib import messages


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
            
    form = ContactForm()

    return render(request, 'website/contact.html' , {'form': form})

