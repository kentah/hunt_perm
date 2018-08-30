from django.contrib import admin
from django.contrib.admin.models import LogEntry

from .models import Category, Post


class BlogView(admin.ModelAdmin):
    list_display = ['title', 'category', 'created', 'modified']
    list_filter = ('created', 'title', 'category')
    ordering = ['-modified']


admin.site.register(Post, BlogView)
admin.site.register(Category)
admin.site.register(LogEntry)
