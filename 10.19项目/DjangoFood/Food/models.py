from django.db import models

# Create your models here.

class Foods_type(models.Model):
    label = models.CharField(max_length=32)
    description = models.TextField()
    def __str__(self):
        return self.label
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

from ckeditor.fields import RichTextField

class News(models.Model):
    title = models.CharField(max_length=32)
    time = models.DateField()
    description = RichTextField()
    image = models.ImageField(upload_to="img/upload")
    content = RichTextField()
    type = models.CharField(max_length=32)

    def __str__(self):
        return self.title