from django.urls import path
from .views import *

urlpatterns = [
    path('', index, name='home'),
    path('blog', blog, name='blog'),
    # path('shop/', shop, name='shop'),
    path('shop/', Shop.as_view(), name='shop'),
    path('shop/subcategory/<slug:slug>', ShopBySubCategory.as_view(), name='shop_subcategory'),
    path('shop/category/<slug:slug>', ShopCategory.as_view(), name='shop_category'),
    path('shop/category/clothing', ShopClothingCategory.as_view(), name='shop_clothing'),
    path('shop/category/shoes', ShopShoesCategory.as_view(), name='shop_shoes'),
    path('shop/category/accessories', ShopAccessoriesCategory.as_view(), name='shop_accessories'),
    path('shop/on-sale', ItemsOnSale.as_view(), name='on_sale'),
    path('shop/brand/<slug:slug>', ShopByBrand.as_view(), name='shop_brand'),
    path('shop/<slug:slug>/', ItemDetail.as_view(), name='single_product')

]
