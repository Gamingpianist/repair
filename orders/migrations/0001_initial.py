# Generated by Django 3.0.5 on 2020-05-08 11:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('appliances', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(verbose_name='下单日期')),
                ('status', models.CharField(choices=[('0', '待付款'), ('1', '待维修'), ('2', '已完成')], max_length=10, verbose_name='订单状态')),
                ('price', models.FloatField(verbose_name='维修价格')),
                ('address', models.TextField(verbose_name='地址')),
                ('content', models.TextField(verbose_name='问题描述')),
                ('appliance', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appliances.Appliance', verbose_name='家电名称')),
            ],
            options={
                'verbose_name': '订单信息',
                'verbose_name_plural': '订单信息',
            },
        ),
    ]
