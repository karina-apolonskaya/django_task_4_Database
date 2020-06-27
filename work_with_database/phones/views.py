from django.shortcuts import render

from phones.models import Phone


def show_catalog(request):
    template = 'catalog.html'
    phones = Phone.objects.all()
    sort_by = request.GET.get("sort")
    if sort_by == "name":
        phones = phones.order_by('name')
    if sort_by == "min_price":
        phones = phones.order_by('price')
    if sort_by == "max_price":
        phones = phones.order_by('-price')
    context = {"phone": phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'
    phone_model = Phone.objects.filter(slug=slug)
    phone_name = phone_model.get().name
    phone_price = phone_model.get().price
    phone_img = phone_model.get().image
    phone_date = phone_model.get().release_date
    phone_lte = phone_model.get().lte_exists

    context = {'phone_model': phone_model,
               'phone_name': phone_name,
               'phone_price': phone_price,
               'phone_img': phone_img,
               'phone_date': phone_date,
               'phone_lte': phone_lte
               }
    return render(request, template, context)


# def index(request):
#     sort_by = request.GET.get("sort", "name")
#     phones = Phone.objects.all()
#     if sort_by["sort"] == "name":
#
#     return render_to_response('index.html')