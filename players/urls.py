from django.urls import path
from players import views

urlpatterns = [
    path('', views.players, name='players'),
    path('<int:id>', views.player_detail, name='player_detail'),
    path('search', views.search, name='search'),
]