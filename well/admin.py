from django.contrib import admin
from . models import People
# Register your models here.

admin.site.site_header = "test login and register"

admin.site.register(People)