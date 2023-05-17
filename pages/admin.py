from django.contrib import admin
from .models import Member
from django.utils.html import format_html
# Register your models here.


class MemberAdmin(admin.ModelAdmin):
    def thumbnail(self, object):
        return format_html('<img src="{}" width="40" style="border-radius: 20px;"/>'.format(object.photo.url))

    thumbnail.short_description = 'photo'

    list_display = ('id', 'thumbnail', 'first_name', 'last_name', 'description', 'created_date')
    list_display_links = ('thumbnail', 'first_name')
    search_fields = ('first_name', 'last_name', 'description')
    list_filter = ('first_name', 'last_name', 'description')



admin.site.register(Member, MemberAdmin)
