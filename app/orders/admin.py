from django.contrib import admin

from django.contrib import admin
from .models import Order, OrderItem


class OrderItemInline(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']
   


class OrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'first_name', 'last_name','phone', 
                    'address',  'paid','get_total_cost',
                    'created', 'updated']
    list_display_links = ['first_name']
    list_filter = ['paid', 'created', 'updated']
    inlines = [OrderItemInline]

admin.site.register(Order, OrderAdmin)
