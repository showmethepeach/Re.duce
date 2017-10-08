from django.contrib import admin
from owner.models import Shop, Menu

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    model = Shop

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu

