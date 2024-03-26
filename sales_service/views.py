from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, DetailView, CreateView
from .models import InvoiceHeader, InvoiceBody, Payer, Supplier
from .forms import InvoiceHeadersForm, InvoiceBodyFormset

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
    context_object_name = 'header'


# class InvoiceHeadersCreateView(CreateView):
#     model = InvoiceHeader
#     template_name = 'sales_service/invoice_headers_create.html'
#     form_class = InvoiceHeadersForm
#     success_url = reverse_lazy('sales_service:headers-list')


def create_invoice(request):
    if request.method == 'GET':
        formset = InvoiceBodyFormset()
        form = InvoiceHeadersForm()
    elif request.method == 'POST':
        formset = InvoiceBodyFormset(request.POST)
        form = InvoiceHeadersForm(request.POST)
        if form.is_valid():
            payer = Payer.objects.get(pk=form.data["payer"])
            supplier = Supplier.objects.get(pk=form.data["supplier"])
            invoice = InvoiceHeader.objects.create(
                number=form.data["number"],
                date=form.data["date"],
                is_paid=form.data["is_paid"],
                payer=payer,
                supplier=supplier,
            )

        if formset.is_valid():
            total = 0
            for form in formset:
                product = form.cleaned_data.get('product')
                count = form.cleaned_data.get('count')
                uom = form.cleaned_data.get('uom')
                if product and count and uom:
                    amount = float(product.price) * float(count)
                    total += amount
                    InvoiceBody(
                        header=invoice,
                        product=product,
                        count=count,
                        uom=uom,
                        ).save()
            invoice.save()
    context = {
        "title": "Invoice Generator",
        "formset": formset,
        "form": form,
    }
    return render(request, 'sales_service/invoice_headers_create.html', context)