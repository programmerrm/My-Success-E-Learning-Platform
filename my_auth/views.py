import random
import string
from django.shortcuts import redirect
from django.views.generic import CreateView
from django.views import View
from django.contrib.auth import views as auth_view
from django.contrib.auth import authenticate, login, logout
from global_feature .models import Logo, LoginRegisterSideBar
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import UserRegisterForm, UserLoginForm, SubAdminLoginForm
from django.views.generic import FormView
from .models import User

class UserLogin(FormView):
    template_name = 'auth/login.html'
    form_class = UserLoginForm
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context

    def form_valid(self, form):
        number = form.cleaned_data.get('number')
        password = form.cleaned_data.get('password')

        try:
            user = User.objects.get(number=number)
        except User.DoesNotExist:
            messages.error(self.request, 'Invalid number or password')
            return self.form_invalid(form)

        if user.role != 'user' or user.account_type != 'user':
            messages.warning(self.request, 'You must have a user account to log in.')
            return self.form_invalid(form)

        if not user.is_active:
            messages.error(self.request, 'Your account is not active. Please contact support.')
            return self.form_invalid(form)

        if user.is_block:
            messages.error(self.request, 'Your account is blocked. Please contact support.')
            return self.form_invalid(form)

        user = authenticate(self.request, number=number, password=password)
        if user is not None:
            if user.is_staff:
                login(self.request, user)
                messages.success(self.request, 'User logged in successfully')
                return redirect(self.get_success_url())
            else:
                messages.warning(self.request, 'Staff permission denied.')
        else:
            messages.error(self.request, 'Invalid number or password')

        return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class UserLogout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('user_login')

class UserRegister(CreateView):
    template_name = 'auth/register.html'
    form_class = UserRegisterForm
    success_url = reverse_lazy('user_login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context
    
    def form_valid(self, form):
        user_id = ''.join(random.choices(string.digits, k=9))
        user = form.save(commit=False)
        user.user_id = user_id
        user.save()
        
        messages.success(self.request, 'User registered successfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        messages.error(self.request, 'There was an error with your submission')
        return self.render_to_response(context)

class SubAdminLogin(FormView):
    template_name = 'auth/sub_admin_login.html'
    form_class = SubAdminLoginForm
    success_url = reverse_lazy('all_student')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context

    def form_valid(self, form):
        number = form.cleaned_data.get('number')
        password = form.cleaned_data.get('password')
        account_type = form.cleaned_data.get('account_type')

        try:
            user = User.objects.get(number=number)
        except User.DoesNotExist:
            messages.error(self.request, 'Invalid number or password')
            return self.form_invalid(form)

        if user.role != 'sub_admin':
            messages.warning(self.request, 'You must have a sub-admin account to log in.')
            return self.form_invalid(form)

        if user.account_type != account_type:
            messages.error(self.request, f'Your account type does not match. Provided: {account_type}, Expected: {user.account_type}')
            return self.form_invalid(form)

        if not user.is_active:
            messages.error(self.request, 'Your account is not active. Please contact support.')
            return self.form_invalid(form)

        if user.is_block:
            messages.error(self.request, 'Your account is blocked. Please contact support.')
            return self.form_invalid(form)

        user = authenticate(self.request, number=number, password=password)
        if user is not None:
            if user.is_staff:
                login(self.request, user)
                messages.success(self.request, 'Sub Admin logged in successfully')
                return redirect(self.get_success_url())
            else:
                messages.warning(self.request, 'Staff permission denied.')
        else:
            messages.error(self.request, 'Invalid number or password')

        return self.form_invalid(form)

    def form_invalid(self, form):
        context = self.get_context_data(form=form)
        return self.render_to_response(context)

class SubAdminLogout(View):
    def get(self, request, *args, **kwargs):
        logout(request)
        messages.success(request, 'Logout successful')
        return redirect('sub_admin_login')

class PasswordReset(auth_view.PasswordResetView):
    template_name = 'auth/forgot_password/password_reset.html'
    email_template_name = 'auth/forgot_password/password_reset_email.html'
    subject_template_name = 'auth/forgot_password/password_reset_subject.txt'
    success_url = reverse_lazy('password_reset_done')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context

class PasswordResetDone(auth_view.PasswordResetDoneView):
    template_name = 'auth/forgot_password/password_reset_done.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context

class PasswordResetConfirm(auth_view.PasswordResetConfirmView):
    template_name = 'auth/forgot_password/password_rest_confirm.html'
    success_url = reverse_lazy('password_reset_complete')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context

class PasswordResetComplete(auth_view.PasswordResetCompleteView):
    template_name = 'auth/forgot_password/password_rest_complete.html'
    success_url = reverse_lazy('home_page')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['logo'] = Logo.objects.first()
        context['sidebar'] = LoginRegisterSideBar.objects.first()
        return context
