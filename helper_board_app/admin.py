from django.contrib import admin

from .models import Category, Request, Reply

admin.site.register(Category)
admin.site.register(Request)
admin.site.register(Reply)