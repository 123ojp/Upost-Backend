# Generated by Django 3.0.2 on 2020-02-01 04:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('poster', '0004_auto_20200131_2210'),
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('board_id', models.AutoField(primary_key=True, serialize=False)),
                ('board_name', models.CharField(max_length=200)),
                ('isSchoolBoard', models.BooleanField(default=False)),
                ('school_id', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
            ],
        ),
        migrations.CreateModel(
            name='Commit',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('likes', models.IntegerField(default=0)),
                ('text', models.TextField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='School',
        ),
        migrations.AddField(
            model_name='post',
            name='isDelete',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='post_likes',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='commit',
            name='post_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poster.Post'),
        ),
        migrations.AddField(
            model_name='post',
            name='board_id',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='poster.Board'),
        ),
    ]
