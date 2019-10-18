from django.db import models

# Create your models here.

class Foods_type(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()

class Foods(models.Model):
    name= models.CharField(max_length=32)
    price = models.FloatField()
    picture = models.ImageField(upload_to="img")
    description = models.TextField()
    type_id = models.ForeignKey(to=Foods_type,on_delete=models.CASCADE)



class Shop(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img/upload")
    foods_id = models.ManyToManyField(to=Foods)
    description = models.TextField()


class Company(models.Model):
    name = models.CharField(max_length=32)
    picture = models.ImageField(upload_to="img/upload")
    phone = models.CharField(max_length=32)
    fax = models.CharField(max_length=32)
    post_code = models.CharField(max_length=32)
    address = models.TextField()

class News(models.Model):
    title = models.CharField(max_length=32)
    time = models.DateField()
    description = models.TextField()
    image = models.ImageField(upload_to="img/upload")
    content = models.TextField()
    type = models.CharField(max_length=32)