# Generated by Django 4.2.16 on 2024-12-20 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customers', '0019_alter_recording_audio_file_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='customer_level',
            field=models.CharField(choices=[('A', 'A 等级'), ('B', 'B 等级'), ('未知', '未知')], default='未知', max_length=10, verbose_name='客户等级'),
        ),
        migrations.AddField(
            model_name='customer',
            name='discuss_checked',
            field=models.BooleanField(default=False, verbose_name='回家商量下'),
        ),
        migrations.AddField(
            model_name='customer',
            name='discuss_text',
            field=models.TextField(blank=True, default='未知', null=True, verbose_name='回家商量下说明'),
        ),
        migrations.AddField(
            model_name='customer',
            name='reconsider_checked',
            field=models.BooleanField(default=False, verbose_name='再慎重考虑下'),
        ),
        migrations.AddField(
            model_name='customer',
            name='reconsider_text',
            field=models.TextField(blank=True, default='未知', null=True, verbose_name='再慎重考虑下说明'),
        ),
        migrations.AlterField(
            model_name='customer',
            name='is_invited',
            field=models.BooleanField(default=False, verbose_name='是否感兴趣'),
        ),
    ]
