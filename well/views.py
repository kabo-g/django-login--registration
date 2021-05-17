from django.shortcuts import render, redirect 
from . forms import RegisterForm
from . models import People

from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from django.db.models import Q


# Create your views here.

def login_view(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			username = form.cleaned_data.get("username")
			password = form.cleaned_data.get("password")
			user = authenticate(request, username = username, password = password)

			if user is not None:
				login(request, user)
				return redirect(home)
		else:
			messages.error(request, "invalid username or password")
	else:
		form = AuthenticationForm()
	
	context = {"form": form}
	return render(request, "login.html", context)


def reg(request):
	if request.method == "POST":
		reg = RegisterForm(request.POST)
		if reg.is_valid():
			reg.save()

			return redirect(login_view)
	else:
		reg = RegisterForm()


	context = {"register": reg}
	return render(request, "reg.html", context)


@login_required(login_url = "/")
def home(request):
	people = People.objects.all()

	query = request.GET.get("search")
	if query:
		p = People.objects.filter(Q(name__icontains = query) | Q(surname__icontains = query)).order_by("name")
		context = {"query": p}
		return render(request, "home.html", context)
	
	
	return render(request, "home.html", {"people": people})

def logout_view(request):
	logout(request)
	return redirect(login_view)