from django.db import models

from Quser.models import Quser


class BuyCar(models.Model):
    """
    购物车
    """
    car_user = models.CharField(max_length=32)
    goods_name = models.CharField(max_length=32)
    goods_picture = models.ImageField(upload_to= "buyer/images")
    goods_price = models.FloatField()
    goods_number = models.IntegerField()
    goods_total = models.FloatField()
    goods_store = models.IntegerField()
    goods_id = models.IntegerField()

class Pay_order(models.Model):
    """
        订单状态
        未支付0
        未发货1
        已发货2
        签收 3/拒收4
    """
    order_id = models.CharField(max_length=32)
    order_time = models.DateTimeField(auto_now=True)
    order_number = models.IntegerField()#买入商品的条数
    order_total = models.FloatField(default=0)
    order_state = models.IntegerField(default=0)
    order_user = models.ForeignKey(to=Quser,on_delete=models.CASCADE)#买家

class Order_info(models.Model):
    order_id = models.ForeignKey(to=Pay_order,on_delete=models.CASCADE)
    goods_name = models.CharField(max_length=32)
    goods_number = models.IntegerField()#每个商品买入的个数
    goods_price = models.FloatField()
    goods_total = models.FloatField(default=0)
    goods_picture = models.CharField(max_length=32)

    order_store = models.ForeignKey(to=Quser, on_delete=models.CASCADE)#卖家

class History(models.Model):
    user_email = models.CharField(max_length=32)
    goods_id = models.IntegerField()
    goods_name = models.TextField()
    goods_price = models.FloatField()
    goods_picture = models.TextField()

# Create your models here.
