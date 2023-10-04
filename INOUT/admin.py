from django.contrib import admin
from .models import *
# Register your models here.


admin.register(settings_product)(admin.ModelAdmin)
admin.register(settings_uom)(admin.ModelAdmin)
admin.register(settings_supplier_list)(admin.ModelAdmin)
admin.register(settings_purchase_status)(admin.ModelAdmin)
admin.register(settings_payment_status)(admin.ModelAdmin)
admin.register(settings_godown_list)(admin.ModelAdmin)
admin.register(stock_update)(admin.ModelAdmin)
admin.register(outwards_update)(admin.ModelAdmin)

