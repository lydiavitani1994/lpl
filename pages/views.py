from django.shortcuts import render

from players.models import Player, get_field_options
from .models import Member


# Create your views here.
def home(request):
    members = Member.objects.all()
    active_players = Player.objects.order_by('-created_date').filter(is_retire=False)
    retired_players = Player.objects.order_by('-created_date').filter(is_retire=True)
    position_options = get_field_options('position')
    is_retire_options = Player.objects.values_list('is_retire', flat=True).distinct()
    team_options = get_field_options('team')
    data = {
        "members": members,
        "active_players": active_players,
        "retired_players": retired_players,
        "position_options": position_options,
        "is_retire_options": is_retire_options,
        "team_options": team_options
    }
    return render(request, 'pages/home.html', data)


def about(request):
    members = Member.objects.all()

    data = {
        "members": members,
    }
    return render(request, 'pages/about.html', data)


def services(request):
    return render(request, 'pages/services.html')


def contact(request):
    return render(request, 'pages/contact.html')
