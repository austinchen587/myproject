# Generated by Django 4.2.16 on 2024-11-28 10:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0014_recording'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='city',
            field=models.CharField(default='未知', max_length=255, verbose_name='当前所在城市'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='data_source',
            field=models.CharField(choices=[('AI数据', 'AI数据'), ('视频号', '视频号'), ('其他', '其他'), ('国开数据', '国开数据'), ('未知', '未知')], default='未知', max_length=100, verbose_name='数据来源'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='first_day_feedback',
            field=models.CharField(choices=[('满意', '满意'), ('一般', '一般'), ('不考虑', '不考虑'), ('未知', '未知')], default='未知', max_length=20, verbose_name='第一天观后反馈'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='intention',
            field=models.CharField(choices=[('低', '低'), ('中', '中'), ('高', '高'), ('未知', '未知')], default='未知', max_length=20, verbose_name='意向程度'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='major_category',
            field=models.CharField(choices=[('IT', 'IT'), ('非IT', '非IT'), ('未知', '未知')], default='未知', max_length=10, verbose_name='专业类别'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='second_day_feedback',
            field=models.CharField(choices=[('满意', '满意'), ('一般', '一般'), ('不考虑', '不考虑'), ('未知', '未知')], default='未知', max_length=20, verbose_name='第二天观后反馈'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='status',
            field=models.CharField(choices=[('在职', '在职'), ('待业', '待业'), ('未知', '未知')], default='未知', max_length=15, verbose_name='状态'),
        ),
    ]