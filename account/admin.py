from django.contrib import admin
from .models import User, promote_user_to_admin

class UserAdmin(admin.ModelAdmin):
    actions = ['promote_users_to_admin']

    def save_model(self, request, obj, form, change):
        if obj.is_staff and change:
            original_user = User.objects.get(pk=obj.pk)
            if not original_user.is_staff:
                obj.add_bonus()

        super().save_model(request, obj, form, change)

    @admin.action(description='Promote selected users to admin')
    def promote_users_to_admin(self, request, queryset):
        for user in queryset:
            promote_user_to_admin(user)

admin.site.register(User, UserAdmin)
