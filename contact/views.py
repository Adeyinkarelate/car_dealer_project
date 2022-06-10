from django.shortcuts import redirect, render
from .models import Contact
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):
    if request.method == "POST":
        car_id = request.POST['car_id']
        user_id = request.POST['user_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        email = request.POST['email']
        city = request.POST['city']
        state = request.POST['state']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)

            if has_contacted:
                messages.error(
                    request, 'You have already make an inquiry about this car,please wait until  our representative get back to you')
                return redirect('/cars/' + car_id)

        contact = Contact(car_id=car_id, user_id=user_id, car_title=car_title, first_name=first_name, last_name=last_name,
                          customer_need=customer_need, email=email, city=city, state=state, phone=phone, message=message)

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email
        send_mail(
            'New car inquiry',
            'You have a new inquiry for the car ' + car_title +
            ' .Please login to your admin panel for more info',
            'aptechota@hotmail.com',
            [admin_email],
            fail_silently=False
        )

        contact.save()
        messages.success(
            request, 'Your request has been submitted,we will get back to you shortly')
    return redirect('/cars/' + car_id)
