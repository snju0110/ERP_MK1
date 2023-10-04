from django.db import models


# Create your models here.

class settings_product(models.Model):
    brand = models.CharField(max_length=200)
    variant = models.CharField(max_length=200)
    sub_variant = models.CharField(max_length=200)

    def __str__(self):
        return self.sub_variant


class settings_uom(models.Model):
    uom = models.CharField(max_length=200)

    def __str__(self):
        return self.uom


class settings_supplier_list(models.Model):
    supplier = models.CharField(max_length=200)

    def __str__(self):
        return self.supplier


class settings_purchase_status(models.Model):
    purchase_status = models.CharField(max_length=200)

    def __str__(self):
        return self.purchase_status


class settings_payment_status(models.Model):
    payment_status = models.CharField(max_length=200)

    def __str__(self):
        return self.payment_status


class settings_godown_list(models.Model):
    godown_list = models.CharField(max_length=200)

    def __str__(self):
        return self.godown_list


class stock_update(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    hsn_code = models.CharField(max_length=200)
    brand = models.CharField(max_length=200)
    variant = models.CharField(max_length=200)
    sub_variant = models.CharField(max_length=200)
    quantity = models.CharField(max_length=200)
    uom = models.CharField(max_length=200)
    invoice_num = models.CharField(max_length=200)
    supplier_name = models.CharField(max_length=200, null=True)
    purchase_status = models.CharField(max_length=200)
    payment_status = models.CharField(max_length=200)
    godown = models.CharField(max_length=200)
    due = models.CharField(max_length=200)
    added_by = models.CharField(max_length=200)
    price = models.IntegerField()
    cgst = models.IntegerField()
    igst = models.IntegerField()
    sgst = models.IntegerField()
    xtra1 = models.CharField(max_length=200, default='na')
    xtra2 = models.CharField(max_length=200, default='na')

    def __str__(self):
        return self.variant


class outwards_update(models.Model):
    id = models.AutoField(primary_key=True)
    date = models.DateField()
    godown = models.CharField(max_length=200, null=True)
    customer_name = models.CharField(max_length=200, null=True)
    area = models.CharField(max_length=200, null=True)
    ph_num = models.CharField(max_length=200, null=True)
    truck_no = models.CharField(max_length=200, null=True)

    brand = models.CharField(max_length=200, null=True)
    variant = models.CharField(max_length=200, null=True)
    sub_variant = models.CharField(max_length=200, null=True)
    hsn_code = models.CharField(max_length=200, null=True)
    quantity = models.CharField(max_length=200, null=True)
    uom = models.CharField(max_length=200, null=True)
    invoice_num = models.CharField(max_length=200, null=True)
    price = models.IntegerField(null=True)

    due = models.CharField(max_length=200, null=True)
    added_by = models.CharField(max_length=200, null=True)
    cgst = models.IntegerField(null=True)
    igst = models.IntegerField(null=True)
    sgst = models.IntegerField(null=True)
    xtra1 = models.CharField(max_length=200, default='na')
    xtra2 = models.CharField(max_length=200, default='na')

    def __str__(self):
        return self.customer_name
