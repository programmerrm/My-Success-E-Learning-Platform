from django.shortcuts import render
from django.views.generic import TemplateView
from global_futures .models import LogoImage, FooterLogo, SocialMediaIcon, ContactInfoFooter, FooterPaymentMethodImage, FooterCopyRightText

# Create your views here.

class MyLearningTemplateView(TemplateView):
    template_name = 'my_learning/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = LogoImage.objects.first()

        context['footer_logo'] = FooterLogo.objects.first()
        context['footer_social_media_icon'] = SocialMediaIcon.objects.all()
        context['contact_info_footer'] = ContactInfoFooter.objects.first()
        context['payment_method_image'] = FooterPaymentMethodImage.objects.first()
        context['copy_right'] = FooterCopyRightText.objects.first()
        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
