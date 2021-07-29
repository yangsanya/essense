from django.contrib import admin
from django.utils.safestring import mark_safe
from .models import *


class ItemImageAdmin(admin.StackedInline):
    model = ItemImage


class BrandAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CollectionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}
    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)


class SubCategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    list_display = ('id', 'name')
    list_display_links = ('id', 'name')
    search_fields = ('name',)
    list_filter = ('collection',)


class ItemAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name',)}

    inlines = [ItemImageAdmin]

    list_display = (
        'id', 'name', 'brand', 'collection', 'category', 'sub_category', 'description', 'price', 'size', 'on_sale',
        'discount', 'get_image')
    list_display_links = ('id', 'name')
    search_fields = ('name', 'collection', 'category', 'sub_category', 'brand', 'on_sale')
    list_editable = ('description', 'price', 'size', 'on_sale', 'discount')

    fields = (
        'name', 'slug', 'brand', 'collection', 'category', 'sub_category', 'description', 'price', 'size', 'on_sale',
        'discount', 'image',
        'get_image')
    readonly_fields = ('get_image',)
    save_on_top = True

    def get_image(self, obj):
        if obj.image:
            return mark_safe(f'<img src="{obj.image.url}"width="75" height="75">')
        else:
            return 'Фотография не была загружена'

    # def get_parent(self):

    get_image.short_description = 'Фотография'

    class Meta:
        model = Item


@admin.register(ItemImage)
class ItemImageAdmin(admin.ModelAdmin):
    pass


admin.site.register(Brand, BrandAdmin)
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(SubCategory, SubCategoryAdmin)
admin.site.register(Item, ItemAdmin)
