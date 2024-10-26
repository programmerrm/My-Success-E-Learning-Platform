from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import Custome_User_Profile_Info

class UserBaseTemplateView(TemplateView):
    template_name = 'user_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'user_profile_url': self.request.build_absolute_uri('/profile/'),
            'user_referral_url': self.request.build_absolute_uri('/referral/'),
            'user_passbook_url': self.request.build_absolute_uri('/passbook/'),
            'user_withdrawal_url': self.request.build_absolute_uri('/withdrawal/'),
            'user_change_password_url': self.request.build_absolute_uri('/change-password/'),
            'user_address_url': self.request.build_absolute_uri('/address/')
        })
        return context

class AddressTemplateView(UserBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = Custome_User_Profile_Info(instance=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = Custome_User_Profile_Info(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('user_address')
        return render(request, self.template_name, {'form': form})

class ProfileTemplateView(UserBaseTemplateView):
    pass

class ReferralTemplateView(UserBaseTemplateView):
    pass

class PassbookTemplateView(UserBaseTemplateView):
    pass

class WithdrawalTemplateView(UserBaseTemplateView):
    pass

class ChangePasswordTemplateView(UserBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)
