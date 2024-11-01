from django.shortcuts import render
from django.views.generic import TemplateView
from global_futures .models import LogoImage
from .models import Banner_Section, Special_Fuature, Live_Class, Help_Line, Achievement
from global_futures .models import FooterLogo, SocialMediaIcon, ContactInfoFooter, FooterPaymentMethodImage, FooterCopyRightText

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        
        context['logo'] = LogoImage.objects.first()
        banner = Banner_Section.objects.first()
        if banner:
            context['short_title'] = banner.short_title
            context['title'] = banner.title
            context['description'] = banner.description
            context['image'] = banner.image.url

        context['special_fuature'] = Special_Fuature.objects.all()
        context['live_class'] = Live_Class.objects.all()
        context['help_line'] = Help_Line.objects.all()
        context['achievement'] = Achievement.objects.all()

        context['footer_logo'] = FooterLogo.objects.first()
        context['footer_social_media_icon'] = SocialMediaIcon.objects.all()
        context['contact_info_footer'] = ContactInfoFooter.objects.first()
        context['payment_method_image'] = FooterPaymentMethodImage.objects.first()
        context['copy_right'] = FooterCopyRightText.objects.first()

        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())