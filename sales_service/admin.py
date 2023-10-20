from django.contrib import admin
from .models import *


class InvoiceHeaderAdmin(admin.ModelAdmin):
    list_display = ['id', 'number', 'date']


admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Payer)
admin.site.register(Supplier)
admin.site.register(InvoiceBody)
admin.site.register(InvoiceHeader, InvoiceHeaderAdmin)