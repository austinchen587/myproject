# Generated by Django 4.2.16 on 2025-01-26 02:39

from django.db import migrations, models
import hr.models


class Migration(migrations.Migration):

    dependencies = [
        ('hr', '0004_remove_candidate_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(blank=True, null=True, storage=hr.models.get_aliyun_storage, upload_to='candidates/photos/', verbose_name='面试照片'),
        ),
    ]
