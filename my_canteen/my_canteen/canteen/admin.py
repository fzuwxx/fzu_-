from django.contrib import admin

from .models import Canteen, Shop, ShopManager


# 在admin中注册绑定
class CanteenAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['canteen_campus', 'sanitation_level']
    list_display = ['canteen_id', 'canteen_name', 'canteen_campus', 'sanitation_level', 'canteen_active']
    list_editable = ['canteen_name', 'canteen_campus', 'sanitation_level', 'canteen_active']


class ShopAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['shop_name']
    list_display = ['shop_id', 'shop_name', 'shop_active', 'manager', 'canteen']
    list_editable = ['shop_name', 'shop_active', 'manager', 'canteen']


class ShopManagerAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['manager_name']
    list_display = ['manager_id', 'manager_name', 'manager_tel', 'manager_status']
    list_editable = ['manager_name', 'manager_tel']


admin.site.register(Canteen, CanteenAdmin)
admin.site.register(Shop, ShopAdmin)
admin.site.register(ShopManager, ShopManagerAdmin)
