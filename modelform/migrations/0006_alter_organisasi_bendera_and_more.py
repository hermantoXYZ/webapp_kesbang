# Generated by Django 4.2.16 on 2024-11-10 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0005_register_created_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='organisasi',
            name='bendera',
            field=models.ImageField(blank=True, null=True, upload_to='dokumen/bendera/'),
        ),
        migrations.AlterField(
            model_name='organisasi',
            name='lambang_logo',
            field=models.ImageField(blank=True, null=True, upload_to='dokumen/logo/'),
        ),
    ]
