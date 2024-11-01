from django.shortcuts import render
from django.views.generic import TemplateView
from global_futures.models import LogoImage, FooterCopyRightText
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib import messages

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

class AllStudent(SubAdminBaseTemplateView):
    pass

class UpdatedProfile(SubAdminBaseTemplateView):
    pass

class ChangePassword(SubAdminBaseTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = PasswordChangeForm(user=self.request.user)
        return context

    def post(self, request, *args, **kwargs):
        form = PasswordChangeForm(user=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Password change successfully")
        context = self.get_context_data()
        context['form'] = form
        return render(request, self.template_name, context)
