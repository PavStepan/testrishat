from django.contrib import admin
from app_pay.models import Item
# Register your models here.


class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']


admin.site.register(Item, ItemAdmin)
