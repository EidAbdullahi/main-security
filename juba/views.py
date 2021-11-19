from django.db.models.aggregates import Sum
from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from . import forms
from . import models
from django.contrib.auth.models import Group
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
    totalpolice=models.Police.objects.all().count()
    totallogistic=models.Logistic.objects.all().count()
    totalcid=models.CID.objects.all().count()
    totalob=models.OB.objects.all().count()
    mydict={
        'totalpolice':totalpolice,
        'totallogistic':totallogistic,
        'totalob':totalob,
        'totalcid':totalcid,
    }
    return render(request,'juba/admin_dashboard.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_police_view(request):
    return render(request,'juba/admin_police.html')


@login_required(login_url='adminlogin')
def admin_add_police_view(request):
    form1=forms.PoliceForm()
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.PoliceForm(request.POST,request.FILES)
        if form1.is_valid():
            form1.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-police')
    return render(request,'juba/admin_add_police.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_view_police_view(request):
    polices=models.Police.objects.all()
    return render(request,'juba/admin_view_police.html',{'polices':polices})


@login_required(login_url='adminlogin')
def searchpolice_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    polices=models.Police.objects.all().filter(unique_id=int(query))
    return render(request,'juba/search-police-result.html',{'polices':polices})



@login_required(login_url='adminlogin')
def delete_police_view(request,pk):
    police=models.Police.objects.get(id=pk)
    police.delete()
    return redirect('admin-view-police')

@login_required(login_url='adminlogin')

def update_police_view(request,pk):
    police=models.Police.objects.get(id=pk)
    form1=forms.PoliceForm(instance=police)
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.PoliceForm(request.POST,instance=police) 
        print(form1)
        if form1.is_valid():
            user=form1.save()
            user.save()
            return redirect('admin-view-police')
    return render(request,'juba/admin_update_police.html',context=mydict)




def add_more_crime_view(request,pk):
    
    mydict={'pk':pk}
    if request.method=='POST':
        query = request.POST['query']
        
        report=models.Report.objects.get(id=pk)
        report.crime=report.crime + " , " + query
        report.save()
    
        return redirect('ob-view-report')
    return render(request,'juba/add_more_crime.html',context=mydict)



@login_required(login_url='adminlogin')
def admin_logistic_view(request):
    return render(request,'juba/admin_logistic.html')


@login_required(login_url='adminlogin')
def admin_cid_view(request):
    return render(request,'juba/admin_cid.html')

@login_required(login_url='adminlogin')
def admin_ob_view(request):
    return render(request,'juba/admin_ob.html')


@login_required(login_url='adminlogin')
def admin_add_cid_view(request):
    form1=forms.CIDUserForm()
    form2=forms.CIDExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.CIDUserForm(request.POST)
        form2=forms.CIDExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
           
            f2.save()

            group = Group.objects.get_or_create(name='CID')
            group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-cid')
    return render(request,'juba/admin_add_cid.html',context=mydict)


@login_required(login_url='adminlogin')

def update_cid_view(request,pk):
    cid=models.CID.objects.get(id=pk)
    user=models.User.objects.get(id=cid.user_id)

    form1=forms.CIDUserForm(instance=user)
    form2=forms.CIDExtraForm(instance=cid)
    mydict={'form1':form1,'form2':form2}

    if request.method=='POST':
        form1=forms.CIDUserForm(request.POST,instance=user)
        form2=forms.CIDExtraForm(request.POST,instance=cid)
        print(form1)
        if form1.is_valid() and form2.is_valid():
            user=form1.save()
            user.set_password(user.password)
            user.save()
            f2=form2.save(commit=False)
           
            f2.save()
            return redirect('admin-view-cid')
    return render(request,'juba/admin_update_cid.html',context=mydict)






@login_required(login_url='adminlogin')
def admin_add_ob_view(request):
    form1=forms.OBUserForm()
    form2=forms.OBExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.OBUserForm(request.POST)
        form2=forms.OBExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            group = Group.objects.get_or_create(name='OB')
            group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-ob')
    return render(request,'juba/admin_add_ob.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_view_cid_view(request):
    cids=models.CID.objects.all()
    return render(request,'juba/admin_view_cid.html',{'cids':cids})


@login_required(login_url='adminlogin')
def searchcid_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    cids=models.CID.objects.all().filter(unique_id=int(query))
    return render(request,'juba/search-cid-result.html',{'cids':cids})

@login_required(login_url='adminlogin')
def delete_cid_view(request,pk):
    cid=models.CID.objects.get(id=pk)
    user=models.User.objects.get(id=cid.user_id)
    user.delete()
    cid.delete()
    return redirect('admin-view-cid')



@login_required(login_url='adminlogin')
def admin_view_ob_view(request):
    obs=models.OB.objects.all()
    return render(request,'juba/admin_view_ob.html',{'obs':obs})


@login_required(login_url='adminlogin')
def admin_report_view(request):
    reports=models.Report.objects.all()
    return render(request,'juba/admin_view_report.html',{'reports':reports})


@login_required(login_url='adminlogin')
def searchcrime_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    reports=models.Report.objects.all().filter(unique_id=int(query))
    return render(request,'juba/search-crime-result.html',{'reports':reports})


def searchcrimebyob_view(request):
    # whatever user write in search box we get in query
    query = request.GET['query']
    reports=models.Report.objects.all().filter(unique_id=int(query))
    return render(request,'juba/search-crime-result-ob.html',{'reports':reports})


@login_required(login_url='adminlogin')

def delete_report_view(request,pk):
    report=models.Report.objects.get(id=pk)
    report.delete()
    return redirect('admin-report')



@login_required(login_url='adminlogin')
def admin_add_logistic_view(request):
    form1=forms.LogisticUserForm()
    form2=forms.LogisticExtraForm()
    mydict={'form1':form1,'form2':form2}
    if request.method=='POST':
        form1=forms.LogisticUserForm(request.POST)
        form2=forms.LogisticExtraForm(request.POST)
        if form1.is_valid() and form2.is_valid():
            print("form is valid")
            user=form1.save()
            user.set_password(user.password)
            user.save()

            f2=form2.save(commit=False)
            f2.user=user
            f2.status=True
            f2.save()

            group = Group.objects.get_or_create(name='LOGISTIC')
            group[0].user_set.add(user)
        else:
            print("form is invalid")
        return HttpResponseRedirect('admin-logistic')
    return render(request,'juba/admin_add_logistic.html',context=mydict)

@login_required(login_url='adminlogin')
def admin_view_logistic_view(request):
    logistics=models.Logistic.objects.all()
    return render(request,'juba/admin_view_logistic.html',{'logistics':logistics})

@login_required(login_url='logisticlogin')
@user_passes_test(is_logistic)
def logistic_dashboard_view(request):
    totalpolicesalary=models.Police.objects.aggregate(Sum('salary'))
    totalcidsalary=models.CID.objects.aggregate(Sum('salary'))
    totalobsalary=models.OB.objects.aggregate(Sum('salary'))
    
    mydict={
        'totalpolicesalary':totalpolicesalary['salary__sum'],
        'totalcidsalary':totalcidsalary['salary__sum'],
        'totalobsalary':totalobsalary['salary__sum'],
    }
    return render(request,'juba/logistic_dashboard.html',context=mydict)



@login_required(login_url='cidlogin')
@user_passes_test(is_cid)
def cid_dashboard_view(request):
    totalob=models.OB.objects.all().count()
    totalreport=models.Report.objects.all().count()
    mydict={
        'totalob':totalob,
        'totalreport':totalreport,
    }
    return render(request,'juba/cid_dashboard.html',context=mydict)


@login_required(login_url='cidlogin')
@user_passes_test(is_cid)
def cid_add_report_view(request):
    form1=forms.ReportForm()
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.ReportForm(request.POST,request.FILES)
        if form1.is_valid():
            report=form1.save()
            report.posted_by="CID"
            
            report.reporter_name=str(request.user)
            report.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('cid-view-report')
    return render(request,'juba/cid_add_report.html',context=mydict)

@login_required(login_url='cidlogin')
@user_passes_test(is_cid)
def cid_view_report_view(request):
    reports=models.Report.objects.all()
    mydict={
        'reports':reports,
    }
    return render(request,'juba/cid_view_report.html',context=mydict)




@login_required(login_url='oblogin')
@user_passes_test(is_ob)
def ob_dashboard_view(request):
    totalobreport=models.Report.objects.filter(posted_by="OB").count()
    totalcidreport=models.Report.objects.filter(posted_by="CID").count()
    mydict={
        'totalobreport':totalobreport,
        'totalcidreport':totalcidreport,
    }
    return render(request,'juba/ob_dashboard.html',context=mydict)



@login_required(login_url='oblogin')
@user_passes_test(is_ob)
def ob_add_report_view(request):
    form1=forms.ReportForm()
    mydict={'form1':form1}
    if request.method=='POST':
        form1=forms.ReportForm(request.POST,request.FILES)
        if form1.is_valid():
            report=form1.save()
            report.posted_by="OB"
            
            report.reporter_name=str(request.user)
            report.save()
        else:
            print("form is invalid")
        return HttpResponseRedirect('ob-view-report')
    return render(request,'juba/ob_add_report.html',context=mydict)


@login_required(login_url='oblogin')
@user_passes_test(is_ob)
def ob_view_report_view(request):
    reports=models.Report.objects.all().filter(posted_by="OB")
    mydict={
        'reports':reports,
    }
    return render(request,'juba/ob_view_report.html',context=mydict)


@login_required(login_url='logisticlogin')
@user_passes_test(is_logistic)
def logistic_police_view(request):
   polices=models.Police.objects.all()
   return render(request,'juba/logistic_view_police.html',{'polices':polices})

@login_required(login_url='logisticlogin')
@user_passes_test(is_logistic)
def logistic_cid_view(request):
   cids=models.CID.objects.all()
   return render(request,'juba/logistic_view_cid.html',{'cids':cids})

@login_required(login_url='logisticlogin')
@user_passes_test(is_logistic)
def logistic_ob_view(request):
   obs=models.OB.objects.all()
   return render(request,'juba/logistic_view_ob.html',{'obs':obs})










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