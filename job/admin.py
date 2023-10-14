from django.contrib import admin
from .models import Job,Category,Company
# Register your models here.
admin.site.register(Job)
admin.site.register(Company)
admin.site.register(Category)