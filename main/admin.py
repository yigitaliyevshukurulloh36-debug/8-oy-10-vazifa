from django.contrib import admin
from .models import Company, Building, Worker, Comment

admin.site.register([Company, Building, Worker, Comment])