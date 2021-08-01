from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django_filters.views import FilterView
from .models import *
from .filters import *


def blog(request):
    return render(request, template_name='essense/blog.html')


def index(request):
    women_category = SubCategory.objects.filter(collection__name='Women')
    men_category = SubCategory.objects.filter(collection__name='Men')
    kids_category = SubCategory.objects.filter(collection__name='Kids')
    items = Item.objects.all().reverse()
    context = {
        'women_category': women_category,
        'men_category': men_category,
        'kids_category': kids_category,
        'items': items,
    }
    return render(request, template_name='essense/index.html', context=context)


class Shop(ListView):
    template_name = 'essense/shop.html'
    context_object_name = 'items'
    paginate_by = 9
    allow_empty = True
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        women_category = SubCategory.objects.filter(collection__name='Women')
        men_category = SubCategory.objects.filter(collection__name='Men')
        kids_category = SubCategory.objects.filter(collection__name='Kids')
        clothing_subcategories = SubCategory.objects.filter(category__name='Clothing')
        shoes_subcategories = SubCategory.objects.filter(category__name='Shoes')
        accessories_subcategories = SubCategory.objects.filter(category__name='Accessories')
        categories = Category.objects.all()
        brands = Brand.objects.all()

        context['women_category'] = women_category
        context['men_category'] = men_category
        context['kids_category'] = kids_category
        context['clothing_subcategories'] = clothing_subcategories
        context['shoes_subcategories'] = shoes_subcategories
        context['accessories_subcategories'] = accessories_subcategories
        context['brands'] = brands
        context['categories'] = categories

        return context

    def get_ordering(self):
        return self.request.GET.get('orderby', )


class ShopCategory(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(category__slug=self.kwargs['slug'])


class ShopBySubCategory(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(sub_category__slug=self.kwargs['slug'])


class ShopByBrand(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(brand__slug=self.kwargs['slug'])


class ItemsOnSale(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(on_sale=True)


class ItemDetail(DetailView):
    model = Item
    context_object_name = 'item'
    template_name = 'essense/single-product-details.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)

        women_category = SubCategory.objects.filter(collection__name='Women')
        men_category = SubCategory.objects.filter(collection__name='Men')
        kids_category = SubCategory.objects.filter(collection__name='Kids')
        clothing_subcategories = SubCategory.objects.filter(category__name='Clothing')
        shoes_subcategories = SubCategory.objects.filter(category__name='Shoes')
        accessories_subcategories = SubCategory.objects.filter(category__name='Accessories')

        context['women_category'] = women_category
        context['men_category'] = men_category
        context['kids_category'] = kids_category
        context['clothing_subcategories'] = clothing_subcategories
        context['shoes_subcategories'] = shoes_subcategories
        context['accessories_subcategories'] = accessories_subcategories

        return context
