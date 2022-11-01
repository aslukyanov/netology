from django.shortcuts import render, redirect
from phones.models import Phone
from django.utils.text import slugify
from django.http import HttpResponse

def index(request):
    return redirect('catalog')


def show_catalog(request):
    template = 'catalog.html'
    sorting = request.GET.get("sort", 1)
    if sorting == 'name':
        phones = Phone.objects.all().order_by('name').values()
    elif sorting == 'min_price':
        phones = Phone.objects.all().order_by('price').values()
    elif sorting == 'max_price':
        phones = Phone.objects.all().order_by('-price').values()
    else:
        phones = Phone.objects.all()

    context = {
        'phones' : phones,
    }
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone = Phone.objects.filter(slug=slug)
    context = {
        'phone' : phone[0],
    }
    return render(request, template, context)


# def show_phones(request) :
#     phones_objects = Phone.objects.all()
#     phones = [f'{c.id}: {c.name}' for c in phones_objects]
#     return HttpResponse('<br>'.join(phones))

