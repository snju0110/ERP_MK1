# Generated by Django 4.0.8 on 2023-10-04 02:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('INOUT', '0003_stock_update'),
    ]

    operations = [
        migrations.CreateModel(
            name='outwards_update',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('date', models.DateField()),
                ('godown', models.CharField(max_length=200, null=True)),
                ('customer_name', models.CharField(max_length=200, null=True)),
                ('area', models.CharField(max_length=200, null=True)),
                ('ph_num', models.CharField(max_length=200, null=True)),
                ('truck_no', models.CharField(max_length=200, null=True)),
                ('brand', models.CharField(max_length=200, null=True)),
                ('variant', models.CharField(max_length=200, null=True)),
                ('sub_variant', models.CharField(max_length=200, null=True)),
                ('hsn_code', models.CharField(max_length=200, null=True)),
                ('quantity', models.CharField(max_length=200, null=True)),
                ('uom', models.CharField(max_length=200, null=True)),
                ('invoice_num', models.CharField(max_length=200, null=True)),
                ('price', models.IntegerField(null=True)),
                ('due', models.CharField(max_length=200, null=True)),
                ('added_by', models.CharField(max_length=200, null=True)),
                ('cgst', models.IntegerField(null=True)),
                ('igst', models.IntegerField(null=True)),
                ('sgst', models.IntegerField(null=True)),
                ('xtra1', models.CharField(default='na', max_length=200)),
                ('xtra2', models.CharField(default='na', max_length=200)),
            ],
        ),
    ]
