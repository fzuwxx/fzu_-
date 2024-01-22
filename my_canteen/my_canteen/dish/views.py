from django.shortcuts import render
import random
from .forms import ChooseTableForm, EvaluateForm
from .models import Shop, Dish, Orders
from customer.models import Customer
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import render, get_object_or_404, redirect


# Create your views here.


def show_dish(request, shop_id):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')
    template_name = 'dish/dish_list.html'
    context = {
        'shop': Shop.objects.filter(shop_id=shop_id),
        'dish_list': Dish.objects.all(),
    }

    return render(request, template_name, context)


def show_order(request):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    template_name = 'dish/my_order.html'

    user_id = request.session['user_id']

    context = {
        'order_list': Orders.objects.filter(customer_id=user_id),
    }
    return render(request, template_name, context)


def show_complete_order(request, order_id):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    template_name = 'dish/my_order.html'

    user_id = request.session['user_id']
    order = get_object_or_404(Orders, order_id=order_id)
    order.evaluation_status = request.session['evaluation_star']
    order.eva_content = request.session['content']
    order.save()
    context = {
        'order_list': Orders.objects.filter(customer_id=user_id),
    }
    return render(request, template_name, context)


def get_order(request, dish_id):
    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')
    dish = get_object_or_404(Dish, dish_id=dish_id)
    user_id = request.session['user_id']
    dish_quantity = int(request.session['quantity'])
    try:
        user = Customer.objects.filter(customer_id=user_id).first()
        order = Orders.objects.create(dish=dish, customer=user)
        price = int(order.dish.dish_price)
        total_price = price * dish_quantity
        order.order_price = total_price
        order.table_numbers = request.session['table_number']
        order.dish_quantity = request.session['quantity']
        order.order_status = 0
        order.save()
        messages.success(request, '下单成功，订单号为 (Order ID-{}). 请支付 {} 元'.format(order.order_id, order.order_price))
        return redirect("dish:show_order")

    except ObjectDoesNotExist:
        messages.warning(request, "你还没有订单哦~")
        return redirect("dish:show_order")


def choose_table(request, dish_id):

    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    choose_form = ChooseTableForm()
    user_id = request.session['user_id']
    dish_id = dish_id
    if request.method == "POST":
        choose_form = ChooseTableForm(request.POST)
        if choose_form.is_valid():
            request.session['quantity'] = choose_form.cleaned_data['quantity']
            request.session['table_number'] = choose_form.cleaned_data['table_numbers']
            try:
                return redirect("dish:get_order", dish_id)
            except Exception as e:
                messages.warning(request, '订单添加失败: {}'.format(str(e)))
    return render(request, 'dish/choose_table.html', locals())


def evaluate(request, order_id):

    if not request.session.get('is_login', None):
        messages.warning(request, "请先登录顾客账户~")
        return redirect('/customer/login/')

    evaluate_form = EvaluateForm()
    order_id = order_id
    if request.method == "POST":
        evaluate_form = EvaluateForm(request.POST)
        if evaluate_form.is_valid():
            request.session['evaluation_star'] = evaluate_form.cleaned_data['evaluation_star']
            request.session['content'] = evaluate_form.cleaned_data['content']
            try:
                return redirect("dish:show_complete_order", order_id)
            except Exception as e:
                messages.warning(request, '订单添加失败: {}'.format(str(e)))
    return render(request, 'dish/evaluation.html', locals())
