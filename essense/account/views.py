from django.shortcuts import render
from mysite.models import Collection


def login(request):
    collections = Collection.objects.all()
    context = {
        'collections': collections
    }

    return render(request, template_name='account/login.html', context=context)
