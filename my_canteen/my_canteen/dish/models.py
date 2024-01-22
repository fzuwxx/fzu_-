from django.db import models
from django.urls import reverse
from canteen.models import Shop
from customer.models import Customer


class Dish(models.Model):
    dish_id = models.AutoField(primary_key=True, verbose_name='菜品编号')
    shop = models.ForeignKey(Shop, models.CASCADE, verbose_name='窗口')
    dish_name = models.CharField(max_length=20, verbose_name='菜品名称')
    dish_detail = models.CharField(max_length=200, blank=True, null=True, verbose_name='菜品描述')
    dish_price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="菜品价格")
    dish_photo = models.ImageField(upload_to='images/dish', null=True, blank=True, verbose_name='菜品照片')
    dish_active = models.IntegerField(choices=[(1, '销售中'),(0, '售罄')], verbose_name='菜品状态')

    class Meta:
        ordering = ['dish_id']
        db_table = 'dish'
        verbose_name = "菜品信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.dish_name

    def get_order_url(self):
        return reverse("dish:get_order", kwargs={'dish_id': self.dish_id})


class Orders(models.Model):
    order_id = models.AutoField(primary_key=True, verbose_name='订单编号')
    dish = models.ForeignKey(Dish, models.CASCADE, verbose_name='菜品')
    customer = models.ForeignKey(Customer, models.CASCADE, verbose_name='顾客')
    table_numbers = models.CharField(max_length=20, default=0, verbose_name='桌号')
    dish_quantity = models.PositiveIntegerField(default=1, verbose_name='份数')
    order_price = models.DecimalField(max_digits=5, decimal_places=2,  blank=True, null=True, verbose_name="订单价格")
    evaluation_status = models.IntegerField(default=0, verbose_name='评价星级')
    eva_content = models.CharField(max_length=255, default='未进行评价', verbose_name='评价内容')
    order_status = models.IntegerField(choices=[(0, '已下单'), (1, '已送出'), (2, '已送达'), (3, '已评价')], default=0, verbose_name='订单状态')
    order_time = models.DateTimeField(auto_now_add=True, verbose_name='下单时间')

    class Meta:
        ordering = ['-order_time']
        db_table = 'orders'
        verbose_name = "订单信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_id)
