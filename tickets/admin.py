from django.contrib import admin

# Register your models here.
from .models import Ticket, Category, Chat
# Register your models here.
admin.site.register(Ticket)
admin.site.register(Category)
admin.site.register(Chat)

