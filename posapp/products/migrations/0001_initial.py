# Generated by Django 4.2.5 on 2023-09-26 06:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nevado',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('tipo', models.CharField(max_length=255)),
                ('vaso', models.PositiveIntegerField(default=1)),
                ('pitillo', models.PositiveBigIntegerField(default=1)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Taco',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('carne', models.CharField(max_length=255)),
                ('pesocarne', models.DecimalField(decimal_places=0, max_digits=5)),
                ('precio', models.DecimalField(decimal_places=0, max_digits=10)),
            ],
        ),
    ]
