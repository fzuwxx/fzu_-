from django.contrib import admin

from .models import Customer


# 在admin中注册绑定
class CustomerAdmin(admin.ModelAdmin):
    list_per_page = 10
    search_fields = ['studentID']
    list_display = ['customer_id', 'campus', 'customer_name',  'studentID', 'customer_tel',
                    'customer_status', 'create_time']
    actions_on_top = True


admin.site.register(Customer, CustomerAdmin)

admin.site.site_header = '校园食堂后台管理系统'
admin.site.site_title = '校园食堂后台管理系统'
