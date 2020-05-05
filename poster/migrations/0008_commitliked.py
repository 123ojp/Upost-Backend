# Generated by Django 3.0.2 on 2020-02-02 00:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poster', '0007_liked'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommitLiked',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isLike', models.BooleanField(default=True)),
                ('commit_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poster.Commit')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]