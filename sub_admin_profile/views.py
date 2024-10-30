from django.shortcuts import render
from django.views.generic import TemplateView
from global_futures .models import LogoImage

# Create your views here.

class IndexView(TemplateView):
    template_name = 'sub_admin_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = LogoImage.objects.first()

        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())
    