# Generated by Django 4.2.16 on 2024-11-14 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0011_alter_customer_student_batch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='education',
            field=models.CharField(choices=[('大专以下', '大专以下'), ('大专', '大专'), ('本科', '本科'), ('研究生及以上', '研究生及以上'), ('未知', '未知')], default='未知', max_length=20, verbose_name='学历'),
        ),
    ]