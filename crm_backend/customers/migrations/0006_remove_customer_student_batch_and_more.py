# Generated by Django 5.1.1 on 2024-10-16 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0005_customer_cloud_computing_promotion_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='student_batch',
        ),
        migrations.RemoveField(
            model_name='customer',
            name='survey_options',
        ),
        migrations.AlterField(
            model_name='customer',
            name='address',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='就业意向城市'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_day_feedback',
            field=models.CharField(choices=[('满意', '满意'), ('一般', '一般'), ('不考虑', '不考虑')], default='一般', max_length=20, verbose_name='第一天观后反馈'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='second_day_feedback',
            field=models.CharField(choices=[('满意', '满意'), ('一般', '一般'), ('不考虑', '不考虑')], default='一般', max_length=20, verbose_name='第二天观后反馈'),
        ),
    ]