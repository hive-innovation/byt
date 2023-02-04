# Generated by Django 4.1.1 on 2022-10-06 10:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='post',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('post', models.CharField(max_length=258)),
                ('date_created', models.DateTimeField()),
                ('post_image', models.ImageField(blank=True, upload_to='post_images')),
                ('reply', models.CharField(max_length=258)),
                ('likes', models.IntegerField()),
                ('dislikes', models.IntegerField()),
                ('shares', models.IntegerField()),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]