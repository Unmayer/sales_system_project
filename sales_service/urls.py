from django.urls import path
from . import views

app_name = 'sales_service'

urlpatterns = [
    path("", views.HomeView.as_view(), name="home"),
    path("headers/add/", views.InvoiceHeadersCreateView.as_view(), name="headers-add"),
    path("headers/<slug:slug>/", views.InvoiceHeadersDetailView.as_view(), name="headers-detail"),
    path("headers/", views.InvoiceHeadersListView.as_view(), name="headers-list"),
]