from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Player


# Create your views here.
def players(request):
    players = Player.objects.all()
    paginator = Paginator(players, 6)  # each page shows 6 data
    page = request.GET.get('page')
    paged_players = paginator.get_page(page)
    data = {
        "players": paged_players,
    }
    return render(request, 'players/players.html', data)


def player_detail(request, id):
    single_player = get_object_or_404(Player, pk=id)
    data = {
        "single_player": single_player,
    }
    return render(request, 'players/player_detail.html', data)


def search(request):
    players = Player.objects.all()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            players = players.filter(description_icontains=keyword)
    data = {
        "players": players,
    }
    return render(request, 'players/search.html', data)