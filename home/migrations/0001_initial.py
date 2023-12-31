# Generated by Django 4.2.7 on 2023-11-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('koment', models.TextField()),
                ('name', models.CharField(max_length=20)),
                ('mark', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images')),
                ('name', models.TextField()),
                ('title', models.TextField()),
                ('category', models.CharField(max_length=200)),
                ('date', models.DateField()),
            ],
        ),
    ]
