from django.core.paginator import Paginator
from django.shortcuts import render, get_object_or_404

from .models import Player, get_field_options


# Create your views here.
def players(request):
    players = Player.objects.all()
    paginator = Paginator(players, 6)  # each page shows 6 data
    page = request.GET.get('page')
    paged_players = paginator.get_page(page)

    position_options = get_field_options('position')
    is_retire_options = Player.objects.values_list('is_retire', flat=True).distinct()
    team_options = get_field_options('team')

    data = {
        "players": paged_players,
        "position_options": position_options,
        "is_retire_options": is_retire_options,
        "team_options": team_options
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

    position_options = get_field_options('position')
    is_retire_options = Player.objects.values_list('is_retire', flat=True).distinct()
    team_options = get_field_options('team')

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            players = players.filter(description__icontains=keyword)

    if 'position' in request.GET:
        position = request.GET['position']
        if position:
            players = players.filter(position__icontains=position)

    if 'is_retire' in request.GET:
        is_retire = request.GET['is_retire']
        if is_retire:
            players = players.filter(is_retire__iexact=is_retire)

    if 'team' in request.GET:
        team = request.GET['team']
        if team:
            players = players.filter(team__icontains=team)

    if 'min_year' in request.GET:
        min_year = request.GET['min_year']
        max_year = request.GET['max_year']
        if min_year and max_year:
            players = players.filter(first_show_year__gte=min_year, first_show_year__lte=max_year)

    data = {
        "players": players,
        "position_options": position_options,
        "is_retire_options": is_retire_options,
        "team_options": team_options
    }
    return render(request, 'players/search.html', data)