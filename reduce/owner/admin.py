from django.contrib import admin
from owner.models import Shop, Menu, Order, OrderSaleMenu

@admin.register(Shop)
class ShopAdmin(admin.ModelAdmin):
    model = Shop

@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):
    model = Menu

class OrderSaleMenuInline(admin.StackedInline):
    model = OrderSaleMenu

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    model = Order
    inlines = [
        OrderSaleMenuInline,
    ]


