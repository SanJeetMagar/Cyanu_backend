from django.contrib import admin

# Register your models here.
from .models import ChatSession

admin.site.register(ChatSession)