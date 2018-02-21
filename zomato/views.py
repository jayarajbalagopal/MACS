from django.shortcuts import render,redirect
from .forms import UserForm
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .models import UserProfile
from django.contrib.auth.decorators import login_required
# Create your views here.

def SignUp(request,*args,**kwargs):
	if request.method == 'POST':
		form = UserForm(request.POST, request.FILES)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			email = form.cleaned_data.get('email')
			user = User.objects.create_user(username=username,password=password,email=email)
			user.save()
			name = form.cleaned_data.get('name')

			user = authenticate(username=username,password=password)
			login(request,user)

			prof_instance = UserProfile(user=user,name=name,profile_picture=request.FILES['profile_picture'])
			prof_instance.save()


			return redirect('/home')
	else:
		form = UserForm()
	return render(request, 'signup.html', {'form': form})

@login_required(login_url='/login')
def home(request,*args,**kwargs):

	obj = UserProfile.objects.get(user=request.user)
	context = {
		'user':obj
	}
	return render(request,'base.html',context)

def login_user(request,*args,**kwargs):
	context = {
		'error':False,
	}
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		user = authenticate(username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('/home')
		context = {
			'error':True
		}

	return render(request,'login.html',context)


def logout_view(request):
    logout(request)
    return redirect('/home')


