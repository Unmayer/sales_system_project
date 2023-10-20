# Generated by Django 4.2.5 on 2023-10-20 06:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название категории')),
                ('description', models.TextField(blank=True, verbose_name='Описание категории')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Payer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование плательщика')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150, verbose_name='Наименование поставщика')),
                ('address', models.CharField(max_length=255, verbose_name='Адрес')),
                ('phone', models.CharField(max_length=20, verbose_name='Телефон')),
                ('slug', models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название товара')),
                ('description', models.TextField(blank=True, verbose_name='Описание товара')),
                ('price', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Цена товара')),
                ('available', models.BooleanField(verbose_name='Наличие на складе')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='products', to='sales_service.category')),
            ],
        ),
        migrations.CreateModel(
            name='InvoiceHeader',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.IntegerField(unique=True, verbose_name='Номер товарной накладной')),
                ('slug', models.SlugField(max_length=100, unique=True)),
                ('date', models.CharField(max_length=20, verbose_name='Дата составления')),
                ('time_create', models.DateTimeField(auto_now_add=True)),
                ('time_update', models.DateTimeField(auto_now=True)),
                ('is_paid', models.BooleanField(choices=[(0, 'Не оплачено'), (1, 'Оплачено')], default=0, verbose_name='Статус документа')),
                ('payer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='sales_service.payer', verbose_name='Плательщик')),
                ('supplier', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='invoices', to='sales_service.supplier', verbose_name='Поставщик')),
            ],
            options={
                'ordering': ['-number'],
            },
        ),
        migrations.CreateModel(
            name='InvoiceBody',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('count', models.PositiveIntegerField(default=0, verbose_name='Количество')),
                ('uom', models.CharField(max_length=50, verbose_name='Единица измерения')),
                ('header', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='body', to='sales_service.invoiceheader')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='sales_service.product')),
            ],
        ),
    ]