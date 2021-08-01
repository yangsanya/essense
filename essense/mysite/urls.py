from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    # path('shop/', shop, name='shop'),
    path('shop/', Shop.as_view(), name='shop'),
    path('shop/subcategory/<slug:slug>', ShopBySubCategory.as_view(), name='shop_subcategory'),
    path('shop/category/<slug:slug>', ShopCategory.as_view(), name='shop_category'),
    path('shop/on-sale', ItemsOnSale.as_view(), name='on_sale'),
    path('shop/brand/<slug:slug>', ShopByBrand.as_view(), name='shop_brand'),
    path('shop/<slug:slug>/', ItemDetail.as_view(), name='single_product')

]