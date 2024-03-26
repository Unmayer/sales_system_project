from django.forms import ModelForm

from sales_service.models import InvoiceHeader, InvoiceBody, Product, Payer, Supplier
from django.forms import formset_factory


class InvoiceHeadersForm(ModelForm):
    class Meta:
        model = InvoiceHeader
        fields = ['number', 'date', 'is_paid', 'payer', 'supplier']


class InvoiceBodyForm(ModelForm):
    class Meta:
        model = InvoiceBody
        fields = ['product', 'count', 'uom']


InvoiceBodyFormset = formset_factory(InvoiceBodyForm, extra=5)


class ProductGuideForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'available', 'category']


class PayerGuideForm(ModelForm):
    class Meta:
        model = Payer
        fields = ['name', 'address', 'phone']


class SupplierGuideForm(ModelForm):
    class Meta:
        model = Supplier
        fields = ['name', 'address', 'phone']

