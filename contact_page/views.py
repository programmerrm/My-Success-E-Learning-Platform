from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ContactInfo
from .forms import HelpLineContact
from global_futures .models import LogoImage, FooterLogo, SocialMediaIcon, ContactInfoFooter, FooterPaymentMethodImage, FooterCopyRightText

# Create your views here.

class IndexView(TemplateView):
    template_name = 'contact_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        context['form'] = HelpLineContact()
        context['logo'] = LogoImage.objects.first()
        context['footer_logo'] = FooterLogo.objects.first()
        context['footer_social_media_icon'] = SocialMediaIcon.objects.all()
        context['contact_info_footer'] = ContactInfoFooter.objects.first()
        context['payment_method_image'] = FooterPaymentMethodImage.objects.first()
        context['copy_right'] = FooterCopyRightText.objects.first()

        return context
    
    def get(self, request, *args, **kwargs):
        return render(self.request, self.template_name, self.get_context_data())

    def post(self, request, *args, **kwargs):
        form = HelpLineContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')
        return render(request, self.template_name, {'form': form, 'contact_info': ContactInfo.objects.first()})