from django.contrib import admin
from myapp.models import Product, Customer, Profile, Cart, Order, Contacts


@admin.register(Product)
class ProductAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'price', 'quantity', 'category']


@admin.register(Customer)
class CustomerAdminModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'name', 'email', 'address', 'phone', 'state', 'city']


@admin.register(Profile)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']


@admin.register(Cart)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['id', 'user', 'product', 'quantity']


@admin.register(Order)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['id', 'name', 'address', 'creates']


@admin.register(Contacts)
class ProfileAdminModel(admin.ModelAdmin):
    list_display = ['name', 'email', 'message']
