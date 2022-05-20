from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.

def cars(request):
    cars = Car.objects.all()
    paginator = Paginator(cars , 2)
    page = request.GET.get('page')
    paged_car = paginator.get_page(page)
    context ={
        'cars':paged_car,
    }
    return render(request, 'cars/cars.html',context)


def car_detail(request, id=id):
    car = get_object_or_404(Car,id=id)
    context ={
        'car':car
    }
    return render(request,'cars/car_detail.html',context)