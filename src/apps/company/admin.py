from django.contrib import admin

# Register your models here.
from .models import CompanyInfo, OutreachNumber , ContactInfo

admin.site.register(CompanyInfo)
admin.site.register(OutreachNumber)
admin.site.register(ContactInfo)
