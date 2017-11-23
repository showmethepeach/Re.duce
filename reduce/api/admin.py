from django.contrib import admin
from api.models import Review
# Register your models here.

@admin.register(Review)
class ShopAdmin(admin.ModelAdmin):
    model = Review
