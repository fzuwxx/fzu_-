from django.urls import path
from .views import show_dish, show_order, get_order, choose_table, evaluate, show_complete_order

app_name = 'dish'
urlpatterns = [
    path('dish/<slug:shop_id>', show_dish, name='show_dish'),
    path('order/', show_order, name='show_order'),
    path('show_complete_order/<slug:order_id>', show_complete_order, name='show_complete_order'),
    path('get_order/<slug:dish_id>', get_order, name='get_order'),
    path('choose_table/<slug:dish_id>', choose_table, name='choose_table'),
    path('evaluation/<slug:order_id>', evaluate, name='evaluation'),
]
