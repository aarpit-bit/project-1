from django.contrib import admin
from .models import Company, Employee, Project

# Register your models here.

admin.site.register([Company, Employee, Project])


