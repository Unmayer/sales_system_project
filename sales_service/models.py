from django.db import models
from django.urls import reverse
from django.utils.text import slugify


class PaidManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(is_published=InvoiceHeader.Status.PAID)


class Category(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название категории")
    description = models.TextField(blank=True, verbose_name="Описание категории")
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название товара")
    description = models.TextField(blank=True, verbose_name="Описание товара")
    price = models.DecimalField(max_digits=8,  decimal_places=2, verbose_name="Цена товара")
    available = models.BooleanField(verbose_name="Наличие на складе")
    category = models.ForeignKey("Category", related_name="products", on_delete=models.SET_NULL, null=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Payer(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование плательщика")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class Supplier(models.Model):
    name = models.CharField(max_length=150, verbose_name="Наименование поставщика")
    address = models.CharField(max_length=255, verbose_name="Адрес")
    phone = models.CharField(max_length=20, verbose_name="Телефон")
    slug = models.SlugField(max_length=100, unique=True, db_index=True)

    def __str__(self):
        return self.name


class InvoiceBody(models.Model):
    header = models.ForeignKey("InvoiceHeader", on_delete=models.CASCADE, related_name="body")
    product = models.ForeignKey("Product", on_delete=models.PROTECT)
    count = models.PositiveIntegerField(default=0, verbose_name="Количество")
    uom = models.CharField(max_length=50, verbose_name="Единица измерения")

    def __str__(self):
        return f"Товарная строка для накладной №{self.header.number} с товаром {self.product.name}"


class InvoiceHeader(models.Model):
    class Status(models.IntegerChoices):
        NOT_PAID = 0, 'Не оплачено'
        PAID = 1, 'Оплачено'

    number = models.IntegerField(verbose_name="Номер товарной накладной", unique=True)
    slug = models.SlugField(max_length=100, unique=True, db_index=True)
    date = models.CharField(max_length=20, verbose_name="Дата составления")
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_paid = models.BooleanField(choices=Status.choices, default=Status.NOT_PAID, verbose_name="Статус документа")
    payer = models.ForeignKey("Payer", on_delete=models.PROTECT, related_name="invoices", verbose_name="Плательщик")
    supplier = models.ForeignKey("Supplier", on_delete=models.PROTECT, related_name="invoices", verbose_name="Поставщик")

    objects = models.Manager()
    paid = PaidManager()

    class Meta:
        ordering = ['-number']

    def __str__(self):
        return f"{self.number} от {self.date}"

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify('invoice_' + str(self.number))
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("sales_service:headers-detail", kwargs={'slug': self.slug})