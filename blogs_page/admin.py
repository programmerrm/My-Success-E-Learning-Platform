from django.contrib import admin
from .models import BlogModel, Category, Tag

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name',)

@admin.register(BlogModel)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_at')
    list_filter = ('categories', 'tags')
