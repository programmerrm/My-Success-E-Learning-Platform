import random
from django.shortcuts import render
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView
from .forms import User_Register_Form
from .models import User

# Create your views here.

class User_Login_TemplateView(TemplateView):
    template_name = 'account/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)
    
class User_Register_CreateView(CreateView):
    template_name = 'account/user_register/index.html'
    form_class = User_Register_Form
    success_url = reverse_lazy('user_login')

    def generate_unique_user_id(self):
        while True:
            user_id = random.randint(100000, 999999)
            if not User.objects.filter(user_id=user_id).exists():
                return user_id

    def get(self, request, *args, **kwargs):
        form = self.get_form()

        referral_code = kwargs.get('referral_code')

        if referral_code:
            form.fields['referral_code'].initial = str(referral_code)

        return render(request, self.template_name, {'form': form})

    def form_valid(self, form):
        user_id = self.generate_unique_user_id()
        form.instance.user_id = user_id

        return super().form_valid(form)

    def form_invalid(self, form):
        response = super().form_invalid(form)
        return response
    