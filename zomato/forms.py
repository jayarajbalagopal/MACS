from django import forms
from .models import UserProfile
from django.contrib.auth.models import User
from .validators import check_if_name_exists

class UserForm(forms.ModelForm):

	class Meta:
		model = UserProfile
		fields = ['name','profile_picture']
		

	username=forms.CharField(required=True,label='Username',validators=[check_if_name_exists],widget=forms.TextInput(attrs={
                "placeholder":"Username",
                "class":"form-control ",
                "style":"height:50px;margin-bottom:20px;"
                }))

	name=forms.CharField(required=True,label='name',widget=forms.TextInput(attrs={
                "placeholder":"name",
                "class":"form-control ",
                "style":"height:50px;margin-bottom:20px;"
                }))

	email=forms.EmailField(max_length=50,required=True,label='Emailid',widget=forms.EmailInput(attrs={
                "placeholder":"Email",
                "class":"form-control ",
                "style":"height:50px;margin-bottom:20px;"
                }))

	password=forms.CharField(max_length=12,min_length=6,required=True,label='password',widget=forms.PasswordInput(attrs={
                "placeholder":"password",
                "class":"form-control ",
                "style":"height:50px;margin-bottom:20px;"
                }))

	profile_picture = forms.FileField(widget=forms.FileInput(attrs={
                "placeholder":"Upload profile picture",
                "class":"form-control ",
                "style":"height:50px;margin-bottom:20px;"
                }))
        
