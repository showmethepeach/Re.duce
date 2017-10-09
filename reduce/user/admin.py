from django.contrib import admin
from user.models import User, Customer, Owner
# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    model = User

@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    model = Customer

@admin.register(Owner)
class OwnerAdmin(admin.ModelAdmin):
    model = Owner
