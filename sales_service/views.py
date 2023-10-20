from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import InvoiceHeader
from .forms import InvoiceHeadersForm

app_name = 'sales_service'


class HomeView(TemplateView):
    template_name = 'sales_service/home.html'


class InvoiceHeadersListView(ListView):
    model = InvoiceHeader
    template_name = 'sales_service/invoice_headers_list.html'
    paginate_by = 20
    context_object_name = 'headers'


class InvoiceHeadersDetailView(DetailView):
    model = InvoiceHeader
    template_name = 'sales_service/invoice_headers_detail.html'


class InvoiceHeadersCreateView(CreateView):
    model = InvoiceHeader
    template_name = 'sales_service/invoice_headers_create.html'
    form_class = InvoiceHeadersForm
    success_url = reverse_lazy('sales_service:headers-list')