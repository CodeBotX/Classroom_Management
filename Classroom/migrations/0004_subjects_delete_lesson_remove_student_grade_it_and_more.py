# Generated by Django 4.2.6 on 2023-12-11 17:07

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Classroom', '0003_alter_student_student_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(choices=[('A', 'Math'), ('B', 'English'), ('C', 'Physics'), ('D', 'Chemistry'), ('E', 'Literature'), ('F', 'IT')], max_length=1)),
                ('score', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
            ],
        ),
        migrations.DeleteModel(
            name='Lesson',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_IT',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_Math',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_chemistry',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_english',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_literature',
        ),
        migrations.RemoveField(
            model_name='student',
            name='grade_physics',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_comment',
        ),
        migrations.RemoveField(
            model_name='student',
            name='student_id',
        ),
        migrations.RemoveField(
            model_name='teacher',
            name='teacher_id',
        ),
        migrations.AlterField(
            model_name='student',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False, validators=[django.core.validators.MinValueValidator(100000), django.core.validators.MaxValueValidator(999999)]),
        ),
        migrations.AddField(
            model_name='subjects',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Classroom.student'),
        ),
    ]