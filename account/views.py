import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import views as auth_views
from .forms import User_Register_Form, User_Login_Form, Sub_Admin_Login_Form, ResetPasswordForm
from global_futures .models import Login_Register_Side_Bar
from .models import User

# Create your views here.

class User_Login_TemplateView(TemplateView):
    template_name = 'account/user_login/index.html'

    def get(self, request, *args, **kwargs):
        form = User_Login_Form()
        side_bar = Login_Register_Side_Bar.objects.first()
        return render(request, self.template_name, {'form': form, 'side_bar': side_bar})

    def post(self, request, *args, **kwargs):
        form = User_Login_Form(request.POST)
        side_bar = Login_Register_Side_Bar.objects.first()

        if form.is_valid():
            number = form.cleaned_data.get('number')
            password = form.cleaned_data.get('password')

            user = authenticate(request, number=number, password=password)

            if user:
                if user.role == 'USER':
                    if user.is_staff and user.is_banned == False:
                        login(request, user)
                        messages.success(request, 'User logged in successfully!')
                        return redirect('home_page')
                    else:
                        messages.warning(request, "Please acitave your account!")
                else:
                    messages.error(request, 'Access denied: you do not have permission to log in.')
            else:
                messages.error(request, 'Invalid number or password.')
        else:
            messages.error(request, 'Please fill in all fields.')

        return render(request, self.template_name, {'form': form, 'side_bar': side_bar})

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
        side_bar = Login_Register_Side_Bar.objects.first()

        referral_code = kwargs.get('referral_code')

        if referral_code:
            form.fields['referral_code'].initial = str(referral_code)

        return render(request, self.template_name, {'form': form, 'side_bar': side_bar})

    def form_valid(self, form):
        user_id = self.generate_unique_user_id()
        form.instance.user_id = user_id
        messages.success(self.request, 'User Register successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        side_bar = Login_Register_Side_Bar.objects.first()
        return render(self.request, self.template_name, {'form': form, 'side_bar': side_bar})

class Sub_Admin_Login_TemplateView(TemplateView):
    template_name = 'account/sub_admin_login/index.html'
    
    def get(self, request, *args, **kwargs):
        form = Sub_Admin_Login_Form()
        side_bar = Login_Register_Side_Bar.objects.first()
        return render(request, self.template_name, {'form': form, 'side_bar': side_bar})
    
    def post(self, request, *args, **kwargs):
        form = Sub_Admin_Login_Form(request.POST)
        side_bar = Login_Register_Side_Bar.objects.first()

        if form.is_valid():
            number = form.cleaned_data.get('number')
            password = form.cleaned_data.get('password')
            account_type = form.cleaned_data.get('account_type')

            user = authenticate(request, number=number, password=password)

            if user:
                if user.role == 'SUB_ADMIN' and user.account_type == account_type:
                    login(request, user)
                    messages.success(request, 'Sub Admin logged in successfully!')
                    return redirect('all_student')
                else:
                    messages.error(request, 'Access denied: you do not have permission to log in.')
            else:
                messages.error(request, 'Invalid number or password.')

        else:
            messages.error(request, 'Please fill in all fields.')

        return render(request, self.template_name, {'form': form, 'side_bar': side_bar})

class User_Logout_View(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('user_login')
    
class Sub_Admin_Logout_View(View):

    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('sub_admin_login')
    
class PasswordResetView(auth_views.PasswordResetView):
    template_name = 'account/forgot_password/password_reset.html'
    email_template_name = 'account/forgot_password/password_reset_email.html'
    subject_template_name = 'account/forgot_password/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['side_bar'] = Login_Register_Side_Bar.objects.first()  # Add your sidebar object here
        return context

class PasswordResetDoneView(auth_views.PasswordResetDoneView):
    template_name = 'account/forgot_password/password_reset_done.html'

class PasswordResetConfirmView(auth_views.PasswordResetConfirmView):
    form_class = ResetPasswordForm
    template_name = 'account/forgot_password/password_reset_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

class PasswordResetCompleteView(auth_views.PasswordResetCompleteView):
    template_name = 'account/forgot_password/password_reset_complete.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {'redirect_url': reverse_lazy('home_page')})
