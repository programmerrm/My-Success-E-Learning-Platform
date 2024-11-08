from django.contrib import admin
from .models import Banner, SpecialFeature, HelpLine, LiveClass, AdminHelpLine, Achievement, UserReview

class BannerAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_title', 'image']

class SpecialFeatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'description']

class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['class_topic', 'joining_time', 'join_meeting_url']

class AdminHelpLineAdmin(admin.ModelAdmin):
    list_display = ['number']

class HelpLineAdmin(admin.ModelAdmin):
    list_display = ['team_leader', 'team_leader_whatup_number', 'trainer', 'trainer_whatup_number']

class UserReviewAdmin(admin.ModelAdmin):
    list_display = ['user', 'title', 'description', 'star']

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'description']

# Register your models here.
admin.site.register(Banner, BannerAdmin)
admin.site.register(SpecialFeature, SpecialFeatureAdmin)
admin.site.register(LiveClass, LiveClassAdmin)
admin.site.register(AdminHelpLine, AdminHelpLineAdmin)
admin.site.register(HelpLine, HelpLineAdmin)
admin.site.register(UserReview, UserReviewAdmin)
admin.site.register(Achievement, AchievementAdmin)
