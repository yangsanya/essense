from django.contrib import admin
from django import forms
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django.utils.safestring import mark_safe

from .models import Post


class PostAdminFrom(forms.ModelForm):
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    form = PostAdminFrom
    save_as = True
    save_on_top = True
    list_display = ('id', 'title', 'slug', 'created_at', 'get_photo')
    list_display_links = ('id', 'title')
    search_fields = ('title',)
    readonly_fields = ('created_at', 'get_image')
    fields = ('title', 'slug', 'content', 'photo', 'get_photo', 'created_at')

    def get_photo(self, obj):
        if obj.photo:
            return mark_safe(f'<img src="{obj.photo.url}" width="50">')
        return '-'

    get_photo.short_description = 'Image'
