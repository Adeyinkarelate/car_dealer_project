from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars, 2)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'cars': paged_car,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,
    }
    return render(request, 'cars/cars.html', context)


def car_detail(request, id=id):
    car = get_object_or_404(Car, id=id)
    context = {
        'car': car
    }
    return render(request, 'cars/car_detail.html', context)


def search(request):
    cars = Car.objects.order_by('-created_date')

    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()
    condition_search = Car.objects.values_list(
        'condition', flat=True).distinct()
    transmission_search = Car.objects.values_list('transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__iexact=model)

    if 'transmission' in request.GET:
        transmission = request.GET['transmission']
        if transmission:
            cars = cars.filter(transmission__iexact=transmission)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)

    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_year' in request.GET:
        body_year = request.GET['body_year']
        if body_year:
            cars = cars.filter(body_year__iexact=body_year)

    if 'condition' in request.GET:
        condition = request.GET['condition']
        if condition:
            cars = cars.filter(condition__iexact=condition)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    context = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,
        'condition_search': condition_search,
        'transmission_search':transmission_search,
    }
    return render(request, 'cars/search.html', context)
