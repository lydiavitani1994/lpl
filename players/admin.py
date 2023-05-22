from django.contrib import admin
from django.utils.html import format_html

from players.models import Player


# Register your models here.
class PlayerAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" height="40" style="border-radius: 20px;"/>'.format(object.photo1.url))

    thumbnail.short_description = 'photo'

    list_display = ('game_id', 'thumbnail', 'name', 'position', 'team', 'first_show_year')
    list_display_links = ('thumbnail', 'game_id')
    search_fields = ('game_id', 'name', 'position', 'team')
    list_filter = ('position', 'team', 'first_show_year')
    # list_editable = ('is_retire')


admin.site.register(Player, PlayerAdmin)