# Generated by Django 4.2.11 on 2024-04-03 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='FileName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=200, null=True)),
                ('key', models.CharField(blank=True, max_length=200, null=True)),
                ('word', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
