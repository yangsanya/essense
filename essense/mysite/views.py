from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from django.views.generic.base import View
from django_filters.views import FilterView
from django.http import HttpResponseRedirect
from .models import *
from .filters import *


def index(request):
    items = reversed(Item.objects.all()[9:])
    collections = Collection.objects.all()
    context = {
        'items': items,
        'collections': collections
    }
    return render(request, template_name='essense/index.html', context=context)


def contact(request):
    return render(request, template_name='essense/contact.html')


def regular(request):
    return render(request, template_name='essense/regular-page.html')


def checkout(request):
    return render(request, template_name='essense/checkout.html')


class Shop(ListView):
    template_name = 'essense/shop.html'
    context_object_name = 'items'
    paginate_by = 9
    allow_empty = True
    model = Item

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        categories = Category.objects.all()
        collections = Collection.objects.all()
        brands = Brand.objects.all()

        context['brands'] = brands
        context['categories'] = categories
        context['collections'] = collections

        return context

    def get_ordering(self):
        return self.request.GET.get('orderby', )


class ShopCategory(Shop, ListView):
    template_name = 'essense/shop.html'

    def get_queryset(self):
        return Item.objects.filter(category__slug=self.kwargs['slug'])

    def get_ordering(self):
        return self.request.GET.get('orderby', )


class ShopBySubCategory(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(sub_category__slug=self.kwargs['slug'])

    def get_ordering(self):
        return self.request.GET.get('orderby', )


class ShopByBrand(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(brand__slug=self.kwargs['slug'])

    def get_ordering(self):
        return self.request.GET.get('orderby', )


class ItemsOnSale(Shop, ListView):

    def get_queryset(self):
        return Item.objects.filter(on_sale=True)

    def get_ordering(self):
        return self.request.GET.get('orderby', )


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
