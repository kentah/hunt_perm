from django.core.mail import send_mail, BadHeaderError, EmailMessage
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import ContactForm



def contactView(request):
    template_name = '../templates/contact/contact.html'
    form_class = ContactForm

    if request.method == 'GET':
        form = ContactForm()
    else:
        form = form_class(request.POST)
        if form.is_valid():
            subject = form.cleaned_data['subject']
            from_email = form.cleaned_data['from_email']
            #from_name = form.cleaned_data['from_name']
            #/from_company = form.cleaned_data['from_company']
            message = form.cleaned_data['message']
            try:
                send_mail(subject, message, from_email, ['khoward@huntingtonadsales.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return redirect('success')
    return render(request, template_name, {'form': form})

def successView(request):
    template_name = '../templates/contact/success.html'

    return HttpResponse('Success! Thank you for your message')
