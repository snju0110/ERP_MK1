# Generated by Django 4.2.4 on 2023-08-31 13:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='settings_product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.CharField(max_length=200)),
                ('variant', models.CharField(max_length=200)),
                ('sub_variant', models.CharField(max_length=200)),
            ],
        ),
    ]