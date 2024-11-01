from django.shortcuts import render
from django.views.generic import TemplateView
from global_futures.models import LogoImage, FooterCopyRightText

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
    # This class will inherit from SubAdminBaseTemplateView
    # The specific template can be handled in the index.html
    pass

class UpdatedProfile(SubAdminBaseTemplateView):
    pass

class ChangePassword(SubAdminBaseTemplateView):
    pass
