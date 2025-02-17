# Generated by Django 4.2.16 on 2025-01-05 09:41

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('closed', '0016_alter_clientdata_created_at_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='clientdata',
            name='created_at',
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='registration_date',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='日期'),
        ),
        migrations.AlterField(
            model_name='clientdata',
            name='responsible_person',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='负责人'),
        ),
    ]
