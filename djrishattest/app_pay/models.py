from django.db import models

# Create your models here.


class Item(models.Model):
    """ Модель товара """
    name = models.CharField(verbose_name='Название', max_length=128)
    description = models.TextField(verbose_name='Описание', blank=True)
    price = models.IntegerField(verbose_name='Цена', default=0)

    def __str__(self):
        return self.name

    def get_display_price(self):
        """ Метод отображения с двумя знаками после запятой """
        return "{0:.2f}".format(self.price / 100)
