import django.contrib.admin
from django.contrib import admin
from .models import Performance, Opera, Genre

admin.site.register(Performance)
admin.site.register(Opera)
admin.site.register(Genre)
