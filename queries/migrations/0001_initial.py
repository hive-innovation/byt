# Generated by Django 4.1.1 on 2022-09-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='search_query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('search_query', models.TextField()),
                ('date_of_query', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]