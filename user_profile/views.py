from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from .forms import Custome_User_Profile_Info, WithdrawalRequestForm, User_Profile_Updated
from .models import WithdrawalProcess
from global_futures .models import LogoImage, FooterLogo, SocialMediaIcon, ContactInfoFooter, FooterPaymentMethodImage, FooterCopyRightText

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
        context['logo'] = LogoImage.objects.first()
        context['footer_logo'] = FooterLogo.objects.first()
        context['footer_social_media_icon'] = SocialMediaIcon.objects.all()
        context['contact_info_footer'] = ContactInfoFooter.objects.first()
        context['payment_method_image'] = FooterPaymentMethodImage.objects.first()
        context['copy_right'] = FooterCopyRightText.objects.first()
        return context

class ProfileTemplateView(UserBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = User_Profile_Updated(instance=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        form = User_Profile_Updated(request.POST, instance=request.user)
        if form.is_valid():
            messages.success(request, 'Profile updated successfully!')
            form.save()
            return redirect('user_profile')
        return render(request, self.template_name, {'form': form})

class ReferralTemplateView(UserBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        
        context['user_id'] = user.user_id
        context['full_name'] = f"{user.first_name} {user.last_name}"
        context['email'] = user.email
        
        referred_users = user.referrals.all()
        
        paginator = Paginator(referred_users, 4) 
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)

        context['referred_users'] = page_obj
        context['page_obj'] = page_obj
        
        return context

class PassbookTemplateView(UserBaseTemplateView):
    pass

class WithdrawalTemplateView(UserBaseTemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = WithdrawalRequestForm()
        
        withdrawals_list = WithdrawalProcess.objects.filter(user=self.request.user)
        
        paginator = Paginator(withdrawals_list, 3) 
        page_number = self.request.GET.get('page')
        withdrawals = paginator.get_page(page_number)
        
        context['withdrawals'] = withdrawals
        return context

    def post(self, request, *args, **kwargs):
        form = WithdrawalRequestForm(request.POST)
        if form.is_valid():
            amount = form.cleaned_data['amount']
            user_balance = request.user.balance

            if amount > user_balance:
                messages.error(request, "Insufficient balance to make this withdrawal.")
            else:
                withdrawal = form.save(commit=False)
                withdrawal.user = request.user
                withdrawal.status = 'pending'
                withdrawal.save()

                request.user.balance -= amount
                request.user.save()

                messages.success(request, "Withdrawal request submitted successfully! An admin will review it.")
                return redirect('user_withdrawal')
        else:
            messages.error(request, "There was an error with your withdrawal request.")

        return render(request, self.template_name, {'form': form, 'withdrawals': WithdrawalProcess.objects.filter(user=request.user)})

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
