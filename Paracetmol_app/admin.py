from pyexpat import model
from django.contrib import admin
from .models import Medical, Registation

# Register your models here.
admin.site.register(Medical)
admin.site.register(Registation)
