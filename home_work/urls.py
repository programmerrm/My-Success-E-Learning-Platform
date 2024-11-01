from django.urls import path
from .views import HomeWorkTemplateView

urlpatterns = [
    path('', HomeWorkTemplateView.as_view(), name='home_work'),
]
