from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import User_Register_Form

# Create your views here.

class IndexView(TemplateView):
    template_name = 'account/index.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class User_Register_CreateView(CreateView):
    template_name = 'account/user_register/index.html'
    form_class = User_Register_Form
    success_url = reverse_lazy('user_login')

    def form_valid(self, form):
        return super().form_valid(form)
    
    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response

    def get(self, request, *args, **kwargs):
        form = self.get_form()
        return render(request, self.template_name, {'form': form})