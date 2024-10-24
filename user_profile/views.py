from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth.forms import PasswordChangeForm

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

class ChangePasswordTemplateView(UserBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            # Add message or redirect here if necessary
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

class ProfileTemplateView(UserBaseTemplateView):
    pass

class ReferralTemplateView(UserBaseTemplateView):
    pass

class PassbookTemplateView(UserBaseTemplateView):
    pass

class WithdrawalTemplateView(UserBaseTemplateView):
    pass


class AddressTemplateView(UserBaseTemplateView):
    pass