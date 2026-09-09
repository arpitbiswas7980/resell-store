from django.contrib import admin
from .models import Product, ProductImage, Order

class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 3  # eksathe 3-4te photo add korar row dekhabe

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    inlines = [ProductImageInline]

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('customer_name', 'phone_number', 'product', 'selected_size', 'city', 'order_date')
    search_fields = ('customer_name', 'phone_number', 'pincode')