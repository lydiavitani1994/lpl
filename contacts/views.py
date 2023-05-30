from django.contrib import messages
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect

from contacts.models import Contact


# Create your views here.


def inquiry(request):
    if request.method == 'POST':
        player_id = request.POST['id']
        game_id = request.POST['game_id']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        customer_need = request.POST['customer_need']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']

        if request.user.is_authenticated:
            user_id = request.user.id
            if Contact.objects.filter(user_id=user_id, game_id=game_id).exists():
                messages.error(request, 'You have already sent a message to this player group host, please wait for the host to contact you.')
                return redirect('/players' + player_id)

        contact = Contact(
            game_id=game_id,
            first_name=first_name,
            last_name=last_name,
            user_id=request.user.id,
            player_id=player_id,
            customer_need=customer_need,
            city=city,
            state=state,
            email=email,
            phone=phone,
            message=message
        )

        admin_info = User.objects.get(is_superuser=True)
        send_mail(
            'New LPL Fan Group Request',
            message,
            'fans.lpl777@gmail.com',
            [admin_info.email],
            fail_silently=False
        )

        contact.save()
        messages.success(request, 'Message is sent to the fan group host, you will be contacted shortly.')

        return redirect('/players' + player_id)
