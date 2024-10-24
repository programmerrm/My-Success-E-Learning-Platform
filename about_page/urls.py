from django.urls import path
from .views import AboutPageTemplateView

urlpatterns = [
    path('', AboutPageTemplateView.as_view(), name='about_page'),
]
