from django.shortcuts import render
from django.views import View
from global_feature .models import Logo
from .models import Banner, SpecialFeature, HelpLine, LiveClass, AdminHelpLine, Achievement, UserReview
from global_feature .models import FooterPaymentMethodImage, FooterDescription, SocialMediaIcon, ContactInfoFooter, FooterCopyRightText

# Create your views here.

class HomePage(View):
    template_name = 'home_page/index.html'

    def get(self, request, *args, **kwargs):
        context = {
            'logo': Logo.objects.first(),
            'banner': Banner.objects.first(),
            'special_feature': SpecialFeature.objects.all(),
            'help_line': HelpLine.objects.first(),
            'live_class': LiveClass.objects.all(),
            'admin_help_line': AdminHelpLine.objects.first(),
            'reviews': UserReview.objects.all(),
            'achievement_item': Achievement.objects.all(),
            'payment_method_image': FooterPaymentMethodImage.objects.first(),
            'footer_description': FooterDescription.objects.first(),
            'social_media_icon': SocialMediaIcon.objects.all(),
            'contact_info_footer': ContactInfoFooter.objects.first(),
            'copy_right': FooterCopyRightText.objects.first(),
        }
        return render(request, self.template_name, context)