from django.contrib import admin
from .models import Item

admin.site.register(Item)


class ItemModelAdmin(admin.ModelAdmin):
    list_display = ['id', 'item_name', 'item_desc', 'item_price']
