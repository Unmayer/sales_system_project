from django.urls import path
from sales_service import views, guides_views

app_name = 'sales_service'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("headers/add/", views.create_invoice, name="headers-add"),
    path("headers/<slug:slug>/", views.InvoiceHeadersDetailView.as_view(), name="headers-detail"),
    path("headers/", views.InvoiceHeadersListView.as_view(), name="headers-list"),

    path("products/<slug:slug>/delete/", guides_views.ProductGuideDeleteView.as_view(), name="products-delete"),
    path("products/<slug:slug>/update/", guides_views.ProductGuideUpdateView.as_view(), name="products-update"),
    path("products/add/", guides_views.ProductGuideCreateView.as_view(), name="products-add"),
    path('products/<slug:slug>/', guides_views.ProductGuideDetailView.as_view(), name='products-detail'),
    path('products/', guides_views.ProductGuideListView.as_view(), name='products-list'),

    path("payers/<slug:slug>/delete/", guides_views.PayerGuideDeleteView.as_view(), name="payers-delete"),
    path("payers/<slug:slug>/update/", guides_views.PayerGuideUpdateView.as_view(), name="payers-update"),
    path("payers/add/", guides_views.PayerGuideCreateView.as_view(), name="payers-add"),
    path('payers/<slug:slug>/', guides_views.PayerGuideDetailView.as_view(), name='payers-detail'),
    path('payers/', guides_views.PayerGuideListView.as_view(), name='payers-list'),

    path("supplier/<slug:slug>/delete/", guides_views.SupplierGuideDeleteView.as_view(), name="suppliers-delete"),
    path("supplier/<slug:slug>/update/", guides_views.SupplierGuideUpdateView.as_view(), name="suppliers-update"),
    path("supplier/add/", guides_views.SupplierGuideCreateView.as_view(), name="suppliers-add"),
    path('supplier/<slug:slug>/', guides_views.SupplierGuideDetailView.as_view(), name='suppliers-detail'),
    path('supplier/', guides_views.SupplierGuideListView.as_view(), name='suppliers-list'),
]

