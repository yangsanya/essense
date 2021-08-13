from django.shortcuts import render
from .models import Post
from mysite.models import Category, Collection, Brand
from django.views.generic import ListView, DetailView


class BlogHome(ListView):
    model = Post
    template_name = 'blog/blog.html'
    context_object_name = 'posts'
    paginate_by = 6

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['posts'] = Post.objects.all()
        categories = Category.objects.all()
        collections = Collection.objects.all()
        brands = Brand.objects.all()

        context['brands'] = brands
        context['categories'] = categories
        context['collections'] = collections

        return context

    class Meta:
        ordering = ['-id']


class PostView(DetailView):
    model = Post
    template_name = 'blog/single-blog.html'
    context_object_name = 'post'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        context['related_posts'] = list(reversed(Post.objects.all()))[:4]

        return context
