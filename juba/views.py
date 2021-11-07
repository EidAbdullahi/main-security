from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from . import forms
from django.db import models
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.
def home_view(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect('afterlogin')
    return render(request,'juba/index.html')

#for checking user 
def is_cid(user):
    return user.groups.filter(name='CID').exists()
def is_logistic(user):
    return user.groups.filter(name='LOGISTIC').exists()
def is_ob(user):
    return user.groups.filter(name='OB').exists()


def afterlogin_view(request):
    if is_cid(request.user):
        return redirect('cid-dashboard')

    elif is_logistic(request.user):
        return redirect('logistic-dashboard')

    elif is_ob(request.user):
        return redirect('ob-dashboard')

    else:
        return redirect('admin-dashboard')



@login_required(login_url='adminlogin')

def admin_dashboard_view(request):

    return render(request,'juba/admin_dashboard.html')





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