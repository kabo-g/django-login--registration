from django.urls import path 
from . views import login_view, reg, home, logout_view



urlpatterns = [ 
	path("", login_view, name = "login"),
	path("reg", reg, name = "reg"),
	path("home", home, name = "home"),
	path("logout", logout_view, name = "logout"),
]