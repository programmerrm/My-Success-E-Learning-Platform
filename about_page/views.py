from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class AboutPageTemplateView(TemplateView):
    template_name = 'about_page/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)