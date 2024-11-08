from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.core.paginator import Paginator 
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from .forms import Custome_User_Profile_Info, WithdrawalRequestForm, User_Profile_Updated
from .models import WithdrawalProcess
from global_feature .models import Logo, FooterCopyRightText, ContactInfoFooter, SocialMediaIcon, FooterDescription, FooterPaymentMethodImage

class UserBaseTemplateView(TemplateView):
    template_name = 'user_page/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'user_profile_url': self.request.build_absolute_uri('/profile/').rstrip('/'),
            'user_referral_url': self.request.build_absolute_uri('/referral/').rstrip('/'),
            'user_passbook_url': self.request.build_absolute_uri('/passbook/').rstrip('/'),
            'user_withdrawal_url': self.request.build_absolute_uri('/withdrawal/').rstrip('/'),
            'user_change_password_url': self.request.build_absolute_uri('/change-password/').rstrip('/'),
            'user_address_url': self.request.build_absolute_uri('/address/').rstrip('/')
        })
        context = {
            'logo': Logo.objects.first(),
            'payment_method_image': FooterPaymentMethodImage.objects.first(),
            'footer_description': FooterDescription.objects.first(),
            'social_media_icon': SocialMediaIcon.objects.all(),
            'contact_info_footer': ContactInfoFooter.objects.first(),
            'copy_right': FooterCopyRightText.objects.first(),
        }
        new_path = self.request.path.replace('user', '').strip('/')
        context['new_path'] = new_path

        return context

class ProfileTemplateView(UserBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = User_Profile_Updated(instance=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        form = User_Profile_Updated(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
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
        last_withdrawal = WithdrawalProcess.objects.filter(user=self.request.user).order_by('-created_at').first()
        if last_withdrawal:
            can_withdraw = (timezone.now() - last_withdrawal.created_at).days >= 7
        else:
            can_withdraw = True
        context['can_withdraw'] = can_withdraw
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
                last_withdrawal = WithdrawalProcess.objects.filter(user=request.user).order_by('-created_at').first()
                if last_withdrawal and (timezone.now() - last_withdrawal.created_at).days < 7:
                    messages.error(request, "You cannot make another withdrawal request within 7 days of the last withdrawal.")
                else:
                    withdrawal = form.save(commit=False)
                    withdrawal.user = request.user
                    withdrawal.status = 'pending'
                    withdrawal.created_at = timezone.now()
                    withdrawal.save()
                    request.user.balance -= amount
                    request.user.save()
                    messages.success(request, "Withdrawal request submitted successfully! An admin will review it.")
                    return redirect('user_withdrawal')
        else:
            messages.error(request, "There was an error with your withdrawal request.")
        withdrawals_list = WithdrawalProcess.objects.filter(user=request.user)
        paginator = Paginator(withdrawals_list, 3)
        page_number = request.GET.get('page')
        withdrawals = paginator.get_page(page_number)
        return render(request, self.template_name, {'form': form, 'withdrawals': withdrawals})

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
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, "Your password was successfully updated!")
            return redirect('user_login')
        else:
            messages.error(request, "There was an error with your password change request.")
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)
    