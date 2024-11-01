from django.urls import path
from .views import MyLearningTemplateView

urlpatterns = [
    path('', MyLearningTemplateView.as_view(), name='my_learning'),
]