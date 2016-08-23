from django.contrib import admin
from .models import Album, Song


class AlbumAdmin(admin.ModelAdmin):
    prepopulated_fields = {'': 'artist'}
    list_display = ('album_title', 'artist,')


admin.site.register(Album)
admin.site.register(Song)

