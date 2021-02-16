from django.contrib import admin

# Register your models here.
from .models import Project, Myskill, Contact
admin.site.register(Project)
admin.site.register(Myskill)
admin.site.register(Contact)
