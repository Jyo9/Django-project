from django import forms
from django.contrib.auth.models import User
from app.models import userprofileinfo

class Userform(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model = User
        fields = ('username','email','password')

class userprofileinfoform(forms.ModelForm):
    class Meta():
        model = userprofileinfo
        fields = ('portfolio_site','profile_pic')