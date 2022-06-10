from django.shortcuts import redirect, render
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.


def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by(
        '-created_date').filter(is_featured=True)
    cars = Car.objects.order_by('-created_date')
    # search_fields = Car.objects.values('model','city','year','body_style')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'cars': cars,
        # 'search_fields':search_fields,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_search': body_search,

    }
    return render(request, 'pages/home.html', context)


def about(request):
    teams = Team.objects.all()
    context = {
        'teams': teams
    }
    return render(request, 'pages/about.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST['name']
        phone = request.POST['phone']
        message = request.POST['message']
        subject = request.POST['subject']

        email_subject = f" Message from carzone website regarding {subject}"
        messsage_body = f" Name: {name} \n Phone: {phone} \n Message: {message}"
        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email

        send_mail(
            email_subject,
            messsage_body,
            'aptechota@hotmail.com',
            [admin_email],
            fail_silently=False,
        )
        messages.success(
            request, "Thank you for contacting us, we will get back to you shortly")
        return redirect('contact')
    return render(request, 'pages/contact.html')


def services(request):
    return render(request, 'pages/services.html')
