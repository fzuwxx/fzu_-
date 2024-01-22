from . import views
from django.urls import path
from .views import show_canteen, show_shop


app_name = 'canteen'
urlpatterns = [
    path('', show_canteen, name='canteen'),
    path('shop/<slug:canteen_id>', show_shop, name='shop'),
]
