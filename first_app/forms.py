from django import forms
from django.contrib.auth.models import User
from first_app.models import user_signup,ads_post,track




class userform(forms.ModelForm):
    password=forms.CharField(widget=forms.PasswordInput())

    class Meta():
        model=User
        fields=('username','email','password')


class signupform(forms.ModelForm):
    class Meta():
        model=user_signup
        fields=('Name','Mobile','Address','District','Zip')



class signin(forms.Form):
    Email=forms.EmailField()
    Password=forms.CharField()


class post_ads(forms.ModelForm):
    class Meta():
        model=ads_post
        fields=('title','picture','picture2','picture3','category','bed','bath','kitchen','area','district','divission','address','description','cost','mobile')

class tracker_form(forms.ModelForm):
    class Meta():
        model=track
        fields=('tarcker',)

class aids(forms.Form):
    ids=forms.IntegerField()
