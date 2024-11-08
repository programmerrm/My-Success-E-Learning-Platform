from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from global_feature .models import Logo, FooterCopyRightText
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SubAdminProfile
from my_auth .forms import TrainerCreateForm, TeamLeaderCreateForm, AnySubAdminCreateForm
from django.contrib.auth import get_user_model
from django.utils import timezone
from user_page .forms import WithdrawalRequestForm
from user_page .models import WithdrawalProcess

User = get_user_model()

class SubAdminBaseTemplateView(TemplateView):
    template_name = 'sub_admin/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sub_admin_all_student': self.request.build_absolute_uri('/all-student/'),
            'sub_admin_profile': self.request.build_absolute_uri('/profile/'),
            'sub_admin_change_password': self.request.build_absolute_uri('/change-password/'),
        })
        context['logo'] = Logo.objects.first()
        context['copy_right'] = FooterCopyRightText.objects.first()
        return context

class AnySubAdminCreate(SubAdminBaseTemplateView):
    def get(self, request, *args, **kwargs):
        form = AnySubAdminCreateForm()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = AnySubAdminCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Account create successfully!")
            return redirect('all_sub_admin_info')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

class TrainerCreate(SubAdminBaseTemplateView):
    def get(self, request, *args, **kwargs):
        form = TrainerCreateForm()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TrainerCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Trainer Account create successfully!")
            return redirect('trainer_create')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)
    
class TeamLeaderCreate(SubAdminBaseTemplateView):
    def get(self, request, *args, **kwargs):
        form = TeamLeaderCreateForm()
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

    def post(self, request, *args, **kwargs):
        form = TeamLeaderCreateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Team Leader Account create successfully!")
            return redirect('team_leader_create')
        context = self.get_context_data(**kwargs)
        context['form'] = form
        return self.render_to_response(context)

class AllStudent(SubAdminBaseTemplateView):
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_number = self.request.GET.get('number', None)
        search_user_id = self.request.GET.get('user_id', None)
        
        users = User.objects.all()
        
        if search_number:
            users = users.filter(number=search_number)
        elif search_user_id:
            users = users.filter(user_id=search_user_id)

        paginator = Paginator(users, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj
        return context

class PendingStudent(SubAdminBaseTemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_number = self.request.GET.get('number', None)
        search_user_id = self.request.GET.get('user_id', None)
        
        users = User.objects.filter(is_active=False)
        
        if search_number:
            users = users.filter(number=search_number)
        elif search_user_id:
            users = users.filter(user_id=search_user_id)

        paginator = Paginator(users, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj
        return context

class UpdatedProfile(SubAdminBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = SubAdminProfile(instance=self.request.user)
        return context
    
    def post(self, request, *args, **kwargs):
        form = SubAdminProfile(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Profile updated successfully!')
            return redirect('sub_admin_profile')
        return render(request, self.template_name, {'form': form})

class ChangePassword(SubAdminBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            messages.success(request, "Password change successfully")
            form.save()
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)

class Withdrawal(SubAdminBaseTemplateView):
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

class Passbook(SubAdminBaseTemplateView):
    pass

class MemberInfo(SubAdminBaseTemplateView):
    pass