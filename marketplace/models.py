from django.db import models


class Product(models.Model):
    product_name = models.CharField(default='', max_length=100, null=False, verbose_name='Название товара')
    description = models.CharField(default='', max_length=1000, null=False, verbose_name='Описание товара')
    price = models.DecimalField('Цена', decimal_places=2, null=False, max_digits=8)
    carrency = models.CharField(default='RUB', max_length=10, null=False, verbose_name='Валюта')

    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'

    def __str__(self):
        return  '{} за {}'.format(self.product_name, self.price)