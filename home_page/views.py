from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

class IndexView(TemplateView):
    template_name = 'home_page/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)