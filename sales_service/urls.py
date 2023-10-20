from django.urls import path
from . import views

app_name = 'sales_service'


urlpatterns = [
    path('', views.index)
]