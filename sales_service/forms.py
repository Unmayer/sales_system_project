from django import forms
from django.forms import ModelForm

from .models import InvoiceHeader


class InvoiceHeadersForm(ModelForm):
    class Meta:
        model = InvoiceHeader
        fields = ['number', 'date', 'is_paid', 'payer', 'supplier']