# Generated by Django 2.2.9 on 2020-01-24 05:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academia', '0003_auto_20200124_0444'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='classes',
            name='class_instructor',
        ),
        migrations.AddField(
            model_name='classes',
            name='class_instructor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='teachers', to='academia.Teacher'),
        ),
    ]
