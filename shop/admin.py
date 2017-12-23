from django.contrib import admin


# Register your models here
from shop.models import Category, Product, Order

#
# class ProductAdmin(admin.ModelAdmin):
#     list_display = ['cost', 'category']
#
#
# class OrderAdmin(admin.ModelAdmin):
#     list_display = ['total_cost ', 'created_at', 'delivery_date']


admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Product)