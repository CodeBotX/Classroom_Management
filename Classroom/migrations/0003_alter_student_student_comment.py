# Generated by Django 4.2.6 on 2023-12-02 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Classroom', '0002_student_teacher'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='student_comment',
            field=models.TextField(blank=True, null=True),
        ),
    ]
