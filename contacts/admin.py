from django.contrib import admin

from contacts.models import Contact


# Register your models here.
class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'game_id', 'city', 'timestamp')
    list_display_links = ('id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email', 'game_id')
    list_per_page = 25


admin.site.register(Contact, ContactAdmin)
