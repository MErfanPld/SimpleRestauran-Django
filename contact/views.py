from django.shortcuts import render
from .forms import ContactForm

# Create your views here.

def Countact_us(request):
    contact_form = ContactForm()
    if request.method == 'POST':
        reserve_form = ContactForm(request.POST)
        if reserve_form.is_valid():
            reserve_form.save()
    else:
        contact_form = ContactForm()
    context = {
        "contact_form": contact_form,
    }
    return render(request, 'contact-us/contact.html', context)
