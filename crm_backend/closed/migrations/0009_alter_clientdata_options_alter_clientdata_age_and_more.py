# Generated by Django 4.2.16 on 2025-01-05 08:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closed', '0008_remove_clientdata_analysis_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientdata',
            options={'verbose_name': '客户信息', 'verbose_name_plural': '客户信息列表'},
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='deal_status',
            field=models.CharField(blank=True, choices=[('已成交', '已成交'), ('未成交', '未成交'), ('跟进中', '跟进中'), ('未知', '未知')], max_length=50, null=True, verbose_name='成交情况'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='education',
            field=models.CharField(blank=True, choices=[('小学', '小学'), ('初中', '初中'), ('高中', '高中'), ('大专', '大专'), ('本科', '本科'), ('研究生及以上', '研究生及以上'), ('未知', '未知')], max_length=50, null=True, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='employment_status',
            field=models.CharField(blank=True, choices=[('在职', '在职'), ('待业', '待业'), ('自由职业', '自由职业'), ('未知', '未知')], max_length=50, null=True, verbose_name='就业情况'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='gender',
            field=models.CharField(blank=True, choices=[('男', '男'), ('女', '女'), ('未知', '未知')], max_length=10, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='payment_method',
            field=models.CharField(blank=True, choices=[('微信', '微信'), ('支付宝', '支付宝'), ('银行转账', '银行转账'), ('现金', '现金'), ('未知', '未知')], max_length=50, null=True, verbose_name='支付方式'),
        ),
    ]
