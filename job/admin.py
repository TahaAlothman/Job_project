from django.contrib import admin
from .models import Job, Job_Overview,Category,Company
# Register your models here.
admin.site.register(Job)
admin.site.register(Job_Overview)
admin.site.register(Company)
admin.site.register(Category)