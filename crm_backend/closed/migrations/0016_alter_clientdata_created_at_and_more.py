# Generated by Django 4.2.16 on 2025-01-05 09:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closed', '0015_clientdata_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, verbose_name='创建时间'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='responsible_person',
            field=models.CharField(default='系统管理员', max_length=30, verbose_name='负责人'),
        ),
    ]