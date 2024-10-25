from django.urls import path
from .views import IndexView, BlogByCategoryView, BlogByTagView, SingleBlogTemplateView

urlpatterns = [
    path('all/', IndexView.as_view(), name='blog_page'),
    path('single/<int:id>/', SingleBlogTemplateView.as_view(), name='single_blog'),
    path('categorie/<int:id>/', BlogByCategoryView.as_view(), name='blog_categorie'),
    path('tag/<int:id>/', BlogByTagView.as_view(), name='blog_tag'),
]
