# Generated by Django 3.2.9 on 2022-03-12 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Zvk',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.PositiveIntegerField()),
                ('category', models.CharField(max_length=5)),
                ('type', models.CharField(max_length=5)),
                ('item', models.CharField(max_length=225)),
                ('status', models.CharField(max_length=20)),
                ('start', models.CharField(max_length=40)),
                ('end', models.CharField(max_length=40)),
                ('ready', models.CharField(max_length=20)),
            ],
        ),
    ]