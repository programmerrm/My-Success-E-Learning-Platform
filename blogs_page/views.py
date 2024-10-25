from django.shortcuts import render, get_object_or_404
from django.views.generic import TemplateView, ListView
from django.core.paginator import Paginator
from .models import BlogModel, Category, Tag

class IndexView(ListView):
    template_name = 'blogs_page/index.html'
    model = BlogModel
    paginate_by = 4

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            return BlogModel.objects.filter(title__icontains=query)
        return BlogModel.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_list = self.get_queryset()
        
        if blog_list.exists():
            paginator = Paginator(blog_list, self.paginate_by)
            page_number = self.request.GET.get('page')
            page_obj = paginator.get_page(page_number)
            context['page_obj'] = page_obj
            context['all_blog'] = page_obj

        context['all_categories'] = Category.objects.all()
        context['all_tags'] = Tag.objects.all()
        return context

class BlogByCategoryView(ListView):
    template_name = 'blogs_page/index.html'
    paginate_by = 4

    def get_queryset(self):
        category_id = self.kwargs['id']
        self.category = get_object_or_404(Category, id=category_id)
        return BlogModel.objects.filter(categories=self.category)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['category_name'] = self.category.name
        context['category_count'] = self.get_queryset().count()
        context['all_categories'] = Category.objects.all()
        context['all_tags'] = Tag.objects.all()
        return context



class BlogByTagView(ListView):
    template_name = 'blogs_page/index.html'
    paginate_by = 4

    def get_queryset(self):
        tag_id = self.kwargs['id']
        self.tag = get_object_or_404(Tag, id=tag_id)
        return BlogModel.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tag_name'] = self.tag.name
        context['tag_count'] = self.get_queryset().count()
        context['all_categories'] = Category.objects.all()
        context['all_tags'] = Tag.objects.all()
        return context




class SingleBlogTemplateView(TemplateView):
    template_name = 'blogs_page/single_blog.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        blog_id = self.kwargs['id']
        context['blog'] = get_object_or_404(BlogModel, id=blog_id)
        return context


