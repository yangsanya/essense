from django.db import models
from django.urls import reverse
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.postgres.fields import ArrayField


class Brand(models.Model):
    name = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Collection(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    collection = models.ManyToManyField(Collection, related_name='collection_category')

    def __str__(self):
        return self.name


class SubCategory(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    category = models.ManyToManyField(Category, related_name='category_subcategory')
    collection = models.ManyToManyField(Collection)

    def __str__(self):
        return self.name


class Item(models.Model):
    name = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, blank=True)
    collection = models.ForeignKey(Collection, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    sub_category = models.ForeignKey(SubCategory, on_delete=models.CASCADE, null=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)
    size = ArrayField(models.CharField(max_length=255))
    price = models.PositiveIntegerField()
    on_sale = models.BooleanField(default=0)
    discount = models.PositiveIntegerField(null=True, blank=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('single_product', kwargs={'slug': self.slug})

    def get_sale(self):
        price = int(self.price * (100 - self.discount) / 100)

        return price


class ItemImage(models.Model):
    item = models.ForeignKey(Item, on_delete=models.CASCADE, null=True, related_name='images')
    images = models.ImageField(upload_to='photos/%Y/%m/%d/', null=True)

    def __str__(self):
        return self.item.name
