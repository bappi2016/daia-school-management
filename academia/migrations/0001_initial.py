# Generated by Django 2.2.9 on 2020-01-22 04:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('teachers_name', models.CharField(help_text='Enter a Teachers Name here', max_length=32)),
                ('teachers_speciality', models.CharField(help_text='Enter a Teachers Speciality.e.g. Drawing Instructor', max_length=32)),
                ('teachers_description', models.TextField(help_text='Enter a Teachers Description', max_length=1200)),
                ('teachers_image', models.ImageField(blank=True, null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(help_text='Enter the class Name here', max_length=120)),
                ('class_duration', models.CharField(default='1 Year', help_text='Enter class duration', max_length=30)),
                ('available_seats', models.PositiveIntegerField(default=30)),
                ('class_description', models.TextField(blank=True, max_length=500, null=True)),
                ('course_description', models.TextField(blank=True, max_length=2500, null=True)),
                ('course_type', models.CharField(help_text='Enter the course type here,e.g. Basic', max_length=20)),
                ('class_iamge', models.ImageField(blank=True, null=True, upload_to='')),
                ('class_iamge_detail', models.ImageField(blank=True, null=True, upload_to='')),
                ('class_added_at', models.DateField()),
                ('student_ages', models.IntegerField()),
                ('tution_fee', models.IntegerField(blank=True, null=True)),
                ('class_instructor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academia.Teacher')),
            ],
        ),
    ]
