from django.shortcuts import render, redirect
from django.core.paginator import Paginator
from django.views.generic import TemplateView
from global_futures.models import LogoImage, FooterCopyRightText
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages
from .forms import SubAdminProfile
from django.contrib.auth import get_user_model

User = get_user_model()

class SubAdminBaseTemplateView(TemplateView):
    template_name = 'sub_admin_profile/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({
            'sub_admin_all_student': self.request.build_absolute_uri('/all-student/'),
            'sub_admin_profile': self.request.build_absolute_uri('/profile/'),
            'sub_admin_change_password': self.request.build_absolute_uri('/change-password/'),
        })
        context['logo'] = LogoImage.objects.first()
        context['copy_right'] = FooterCopyRightText.objects.first()
        return context

class PendingStudent(SubAdminBaseTemplateView):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        search_number = self.request.GET.get('number', None)
        search_user_id = self.request.GET.get('user_id', None)
        
        users = User.objects.filter(is_staff=False)
        
        if search_number:
            users = users.filter(phone=search_number)
        if search_user_id:
            users = users.filter(user_id=search_user_id)

        paginator = Paginator(users, 5)
        page_number = self.request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        
        context['page_obj'] = page_obj
        return context

class AllStudent(SubAdminBaseTemplateView):
    pass

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
    pass

class Passbook(SubAdminBaseTemplateView):
    pass
