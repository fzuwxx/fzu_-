from django.shortcuts import render, redirect
from django.contrib import messages
# Create your views here.
from .models import Canteen, Shop


def show_canteen(request):

    template_name = 'canteen/canteen_list.html'
    context = {'canteen_list': Canteen.objects.all()}
    return render(request, template_name, context)


def show_shop(request, canteen_id):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')
    template_name = 'canteen/shop_list.html'
    context = {
        'canteen': Canteen.objects.filter(canteen_id=canteen_id),
        'shop_list': Shop.objects.all()
    }
    return render(request, template_name, context)
