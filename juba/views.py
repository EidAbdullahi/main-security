from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from . import forms
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'juba/index.html')

def aboutus_view(request):
    return render(request,'juba/aboutus.html')

def contactus_view(request):
    sub = forms.ContactusForm()
    if request.method == 'POST':
        sub = forms.ContactusForm(request.POST)
        if sub.is_valid():
            email = sub.cleaned_data['Email']
            name=sub.cleaned_data['Name']
            message = sub.cleaned_data['Message']
            send_mail(str(name)+' || '+str(email),message, settings.EMAIL_HOST_USER, ['wapka1503@gmail.com'], fail_silently = False)
            return render(request, 'juba/contactussuccess.html')
    return render(request, 'juba/contactus.html', {'form':sub})