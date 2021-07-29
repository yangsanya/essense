from django_filters import FilterSet, CharFilter, NumberFilter, OrderingFilter
from .models import Item


CHOICES = [
    ['name', 'по алфавиту'],
    ['price', 'дешевые сверху'],
    ['-price', 'дорогие сверху'],
]


class ItemFilter(FilterSet):
    category__slug = CharFilter()
    price__gt = NumberFilter(name='price', lookup_expr='gt')
    price__lt = NumberFilter(name='price', lookup_expr='lt')
    ordering = OrderingFilter(choices=CHOICES, required=True, empty_label=None)

    class Meta:
        model = Item
        exclude = [field.name for field in Item._meta.fields]
        order_by_field = 'name'
