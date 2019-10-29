from django.db import models
from ckeditor.fields import RichTextField

class Goods(models.Model):
    name = models.CharField(max_length=32)
    price = models.FloatField()
    number = models.IntegerField()
    production = models.DateTimeField()
    safe_date = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="shop/img",default="shop/img/1.jpg")
    description = RichTextField()

    statue = models.IntegerField() #0 下架 1 上架
# Create your models here.
