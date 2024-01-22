from django.contrib import admin

from .models import Dish, Orders


# 在admin中注册绑定
class DishAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['dish_name']
    list_display = ['dish_id', 'dish_name', 'shop', 'dish_price', 'dish_active']
    list_editable = ['dish_name', 'shop', 'dish_price', 'dish_active']


class OrdersAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['evaluation_status']
    list_display = ['order_id', 'dish', 'customer', 'dish_quantity', 'order_price', 'table_numbers',
                    'evaluation_status', 'eva_content', 'order_time']


admin.site.register(Dish, DishAdmin)
admin.site.register(Orders, OrdersAdmin)
# admin.site.register(Comments, CommentsAdmin)
