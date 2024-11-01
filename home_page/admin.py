from django.contrib import admin
from .models import Banner_Section, Special_Fuature, Live_Class, Help_Line, Achievement

class BannerSectionAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_title', 'description', 'image']

class SpecialFuatureAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image']

class LiveClassAdmin(admin.ModelAdmin):
    list_display = ['class_topic', 'joining_time', 'join_meeting_url']

class HelpLineAdmin(admin.ModelAdmin):
    list_display = ['team_leader', 'team_leader_whatup_number', 'telegram_url', 'any_kind_of_problem_date', 'any_kind_of_problem_google_meeting_url']

class AchievementAdmin(admin.ModelAdmin):
    list_display = ['title', 'short_description', 'image']

# Register your models here.
admin.site.register(Banner_Section, BannerSectionAdmin)
admin.site.register(Special_Fuature, SpecialFuatureAdmin)
admin.site.register(Live_Class, LiveClassAdmin)
admin.site.register(Help_Line, HelpLineAdmin)
admin.site.register(Achievement, AchievementAdmin)
