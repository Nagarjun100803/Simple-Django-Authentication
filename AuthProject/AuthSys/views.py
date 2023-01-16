from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from .forms import SignupForm
from django.contrib.auth import authenticate,login as Login,logout as Logout
from django.contrib import messages

# Create your views here.

def home(request):
	return render(request,"AuthSys/home.html")

def signup(request):
	if request.method == "POST":
		form = SignupForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect("login")

	else:
		form = SignupForm()
		return render(request,"AuthSys/signup.html",{'form':form})

def login(request):
	if request.method == "POST":
		username = request.POST["username"]
		password = request.POST["password"]

		user = authenticate(username=username,password=password)
		if user is not None:
			Login(request,user)
			return redirect("home")

		else:
			return redirect("login")
	return render(request,"AuthSys/login.html")

def logout(request):
	Logout(request)
	return redirect("home")



