from urllib.parse import urlencode

from django.shortcuts import render
from django.urls import reverse

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    sort = request.GET.get('sort')
    if sort == 'min_price' or sort == 'max_price' or sort == 'name':
        if sort == 'min_price':
            phones = Phone.objects.order_by('price')
        elif sort == 'max_price':
            phones = Phone.objects.order_by('-price')
        elif sort == 'name':
            phones = Phone.objects.order_by('name')
    else:
        phones = Phone.objects.all()
    phones_list = []
    for phone in phones:
        phones_list.append({
            'name': phone.name,
            'price': phone.price,
            'image': phone.image
        })
    context = {
        'name': phones_list,
        'sort_min_price_url': reverse('catalog') + '?' + urlencode({'sort': 'min_price'}),
        'sort_max_price_url': reverse('catalog') + '?' + urlencode({'sort': 'max_price'}),
        'sort_by_name_url': reverse('catalog') + '?' + urlencode({'sort': 'name'}),
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.get(slug=slug)
    context = {
        'name': phone.name,
        'price': phone.price,
        'release_date': phone.release_date,
        'lte_exists': phone.lte_exists,
        'image': phone.image
    }
    return render(request, template, context)
