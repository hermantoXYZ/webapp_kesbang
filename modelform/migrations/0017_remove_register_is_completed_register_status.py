# Generated by Django 4.2.16 on 2024-11-13 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modelform', '0016_register_is_completed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='register',
            name='is_completed',
        ),
        migrations.AddField(
            model_name='register',
            name='status',
            field=models.CharField(choices=[('draft', 'Draft'), ('completed', 'Completed')], default='draft', max_length=20),
        ),
    ]
