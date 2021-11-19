from django import forms
from django.contrib.auth.models import User
from . import models

#for contact us page
class ContactusForm(forms.Form):
    Name = forms.CharField(max_length=30)
    Email = forms.EmailField()
    Message = forms.CharField(max_length=500,widget=forms.Textarea(attrs={'rows': 3, 'cols': 30}))




class PoliceForm(forms.ModelForm):
    class Meta:
        model=models.Police
        fields='__all__'
class ReportForm(forms.ModelForm):
    class Meta:
        model=models.Report
        fields=['crime_date','criminal_pic','criminal_name','gender','height','unique_id','weight','hair_color','crime']



class LogisticUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class LogisticExtraForm(forms.ModelForm):
    class Meta:
        model=models.Logistic
        fields=['mother_name','mobile','gender']


class CIDUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class CIDExtraForm(forms.ModelForm):
    class Meta:
        model=models.CID
        fields=['mother_name','mobile','gender','salary','district','unique_id']


class OBUserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']
class OBExtraForm(forms.ModelForm):
    class Meta:
        model=models.OB
        fields=['mother_name','mobile','gender','salary']