# Generated by Django 3.0.2 on 2020-02-01 04:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
        ('users', '0003_auto_20200201_0048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unverifyuser',
            name='school',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='schools.School'),
        ),
    ]
