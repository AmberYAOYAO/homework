# Generated by Django 2.2.6 on 2019-11-05 20:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Quser', '0005_goodsaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goodsaddress',
            name='address',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Quser.Quser'),
        ),
    ]
