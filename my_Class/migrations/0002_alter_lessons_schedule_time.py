# Generated by Django 4.2.6 on 2024-01-14 12:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('my_Class', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='lessons',
            name='schedule_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]