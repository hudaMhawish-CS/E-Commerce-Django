from django.contrib import admin
from .models import Order,OrderItem


class OrderItemAdmin(admin.TabularInline):
    model = OrderItem
    raw_id_fields = ['product']


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id','first_name','last_name','address','email','postal_code',)
    list_filter = ('paid','created','updated',)
    search_fields = ['first_name','last_name','email']
    inlines = [OrderItemAdmin]


admin.site.register(Order, OrderAdmin)
