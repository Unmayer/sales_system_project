from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from sales_service.models import Product, Payer, Supplier
from sales_service.forms import ProductGuideForm, PayerGuideForm, SupplierGuideForm


class ProductGuideListView(ListView):
    model = Product
    template_name = 'sales_service/guides/products_list.html'
    context_object_name = 'products'


class ProductGuideDetailView(DetailView):
    model = Product
    template_name = 'sales_service/guides/product_detail.html'
    context_object_name = 'product'


class ProductGuideCreateView(CreateView):
    model = Product
    template_name = 'sales_service/guides/product_create.html'
    form_class = ProductGuideForm
    success_url = reverse_lazy('sales_service:products-list')


class ProductGuideUpdateView(UpdateView):
    model = Product
    form_class = ProductGuideForm
    template_name = 'sales_service/guides/product_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        return context


class ProductGuideDeleteView(DeleteView):
    model = Product
    context_object_name = 'product'
    template_name = 'sales_service/guides/product_delete.html'
    success_url = reverse_lazy('sales_service:products-list')


class PayerGuideListView(ListView):
    model = Payer
    template_name = 'sales_service/guides/payers_list.html'
    context_object_name = 'payers'


class PayerGuideDetailView(DetailView):
    model = Payer
    template_name = 'sales_service/guides/payer_detail.html'
    context_object_name = 'payer'


class PayerGuideCreateView(CreateView):
    model = Payer
    template_name = 'sales_service/guides/payer_create.html'
    form_class = PayerGuideForm
    success_url = reverse_lazy('sales_service:payers-list')


class PayerGuideUpdateView(UpdateView):
    model = Payer
    form_class = PayerGuideForm
    template_name = 'sales_service/guides/payer_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        return context


class PayerGuideDeleteView(DeleteView):
    model = Payer
    context_object_name = 'payer'
    template_name = 'sales_service/guides/payer_delete.html'
    success_url = reverse_lazy('sales_service:payers-list')


class SupplierGuideListView(ListView):
    model = Supplier
    template_name = 'sales_service/guides/suppliers_list.html'
    context_object_name = 'suppliers'


class SupplierGuideDetailView(DetailView):
    model = Supplier
    template_name = 'sales_service/guides/supplier_detail.html'
    context_object_name = 'supplier'


class SupplierGuideCreateView(CreateView):
    model = Supplier
    template_name = 'sales_service/guides/supplier_create.html'
    form_class = SupplierGuideForm
    success_url = reverse_lazy('sales_service:suppliers-list')


class SupplierGuideUpdateView(UpdateView):
    model = Supplier
    form_class = SupplierGuideForm
    template_name = 'sales_service/guides/supplier_update.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['slug'] = self.kwargs.get('slug')
        return context


class SupplierGuideDeleteView(DeleteView):
    model = Supplier
    context_object_name = 'supplier'
    template_name = 'sales_service/guides/supplier_delete.html'
    success_url = reverse_lazy('sales_service:suppliers-list')

