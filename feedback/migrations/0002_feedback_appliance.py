# Generated by Django 3.0.5 on 2020-05-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('feedback', '0001_initial'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='feedback',
            name='appliance',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orders.Order', verbose_name='家电名称'),
        ),
    ]
