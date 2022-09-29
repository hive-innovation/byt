# Generated by Django 4.1.1 on 2022-09-29 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='library',
            fields=[
                ('book_id', models.AutoField(primary_key=True, serialize=False)),
                ('book_title', models.CharField(max_length=288)),
                ('book_description', models.CharField(max_length=1000, null=True)),
                ('book_doc', models.FileField(upload_to='scripts')),
            ],
        ),
    ]
