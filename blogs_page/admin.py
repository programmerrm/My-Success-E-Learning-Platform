from django.contrib import admin
from .models import Category, Tag, BlogModel

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']

class TagAdmin(admin.ModelAdmin):
    list_display = ['name']

class BlogAdmin(admin.ModelAdmin):
    list_display = ['title', 'get_image', 'description', 'display_categories', 'display_tags']
    search_fields = ['title', 'tags__name', 'categories__name']

    def get_image(self, obj):
        return obj.image.url if obj.image else "No Image"
    get_image.short_description = 'Image'

    def display_categories(self, obj):
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'

    def display_tags(self, obj):
        return ", ".join([tag.name for tag in obj.tags.all()])
    display_tags.short_description = 'Tags'

admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(BlogModel, BlogAdmin)
