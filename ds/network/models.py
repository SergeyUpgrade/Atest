from django.core.exceptions import ValidationError
from django.db import models
from django.urls import reverse
from django.utils.safestring import mark_safe


class Product(models.Model):
    name = models.CharField(max_length=255, verbose_name='Название')
    model = models.CharField(max_length=255, verbose_name='Модель')
    release_date = models.DateField(verbose_name='Дата выхода на рынок')

    def __str__(self):
        return f"{self.name} ({self.model})"

    class Meta:
        verbose_name = 'продукт'
        verbose_name_plural = 'продукты'


class NetworkNode(models.Model):
    LEVEL_CHOICES = [
        (0, 'Завод'),
        (1, 'Розничная сеть'),
        (2, 'Индивидуальный предприниматель'),
    ]

    name = models.CharField(max_length=255, verbose_name='Название')
    email = models.EmailField(verbose_name='Почта')
    country = models.CharField(max_length=100, verbose_name='Страна')
    city = models.CharField(max_length=100, verbose_name='Город')
    street = models.CharField(max_length=100, verbose_name='Улица')
    house_number = models.CharField(max_length=10, verbose_name='Номер дома')
    products = models.ManyToManyField(Product, verbose_name='Продукты')
    supplier = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, verbose_name='Поставщик')
    debt = models.DecimalField(max_digits=15, decimal_places=2, default=0, verbose_name='Задолженность перед поставщиком')
    level = models.IntegerField(choices=LEVEL_CHOICES, verbose_name='Уровень в иерархии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'звено сети'
        verbose_name_plural = 'звенья сети'

    def supplier_link(self):
        """
        Функция, чтобы представить поставщика кликабельной ссылкой
        :return:
        """
        if not self.supplier_id:
            return ''
        info = (self.supplier._meta.app_label, self.supplier._meta.model_name)
        admin_url = reverse('admin:%s_%s_change' % info, args=(self.supplier.pk,))
        return mark_safe(f'<a href="{admin_url}">{self.supplier}</a>')

    def clean(self):
        """
        Функция, запрещающая быть поставщиком самого себя
        :return:
        """
        if self.supplier and self.pk and self.supplier_id == self.supplier.pk:
            raise ValidationError({
            'supplier': 'Нельзя быть поставщиком самого себя'
            })
