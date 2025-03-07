# Generated by Django 4.2.16 on 2025-01-04 06:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('closed', '0006_clientdata_customer_summary_clientdata_deal_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientdata',
            name='age',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='年龄'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='analysis',
            field=models.TextField(blank=True, null=True, verbose_name='情况分析'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='customer_summary',
            field=models.TextField(blank=True, null=True, verbose_name='客户总结'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='deal_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='成交情况'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='education',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='学历'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='employment_details',
            field=models.TextField(blank=True, null=True, verbose_name='具体就业情况'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='employment_status',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='就业情况'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='feedback',
            field=models.TextField(blank=True, null=True, verbose_name='问题反馈'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='gender',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='性别'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='is_employed',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='是否就业'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='major',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='专业'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='payment_amount',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='支付金额'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='payment_method',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='支付方式'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='payment_method_detail',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='付款方式'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='phone',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='电话'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='problem_exists',
            field=models.TextField(blank=True, null=True, verbose_name='存在问题'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='remarks',
            field=models.TextField(blank=True, null=True, verbose_name='备注'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='负责人'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='sales_teacher',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='就业老师'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='solution',
            field=models.TextField(blank=True, null=True, verbose_name='解决办法'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='study_progress',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='学习进度'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='study_time',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='学习时间'),
        ),
    ]
