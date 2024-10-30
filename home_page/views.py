from django.shortcuts import render
from django.views.generic import TemplateView
from global_futures .models import LogoImage
from .models import Banner_Section

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

        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())