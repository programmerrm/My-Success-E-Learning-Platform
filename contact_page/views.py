from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import ContactInfo
from .forms import HelpLineContact

# Create your views here.

class IndexView(TemplateView):
    template_name = 'contact_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['contact_info'] = ContactInfo.objects.first()
        context['form'] = HelpLineContact()
        return context

    def post(self, request, *args, **kwargs):
        form = HelpLineContact(request.POST)
        if form.is_valid():
            form.save()
            return redirect('contact_page')
        return render(request, self.template_name, {'form': form, 'contact_info': ContactInfo.objects.first()})