from django.shortcuts import render
from django.views.generic import TemplateView
from .models import ContactInfo

# Create your views here.

class IndexView(TemplateView):
    template_name = 'contact_page/index.html'

    def get_context_data(self, **kwargs):
        context =  super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()

        return context

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, self.get_context_data())