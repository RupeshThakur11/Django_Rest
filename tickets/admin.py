from django.contrib import admin

# Register your models here.
from .models import Ticket, Category, Chat, Genre , Artist, Song , Album
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Chat)
admin.site.register(Genre)
admin.site.register(Artist)
admin.site.register(Song)
admin.site.register(Album)