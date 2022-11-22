from django.test import TestCase
from django.urls import reverse
from app_pay.models import Item


NUMBERS_OF_SHOP = 2


class CreateItem(TestCase):
    """ Класс для заполнения БД тестовыми предметами """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        for i in range(NUMBERS_OF_SHOP):
            Item.objects.create(name=f'товар {i}',
                                description=f'описание {i}',
                                price=1000+int(i+1))


class TestItemDetail(CreateItem):
    """Дочерний класс. Модель тестирования страницы с товаром"""

    def test_item_detail_url_exists_at_desire_location(self):
        response = self.client.get(f'/item/{Item.objects.first().id}/')
        self.assertEqual(response.status_code, 200)

    def test_item_detail_correct_template(self):
        response = self.client.get(reverse('item-detail', kwargs={'pk': Item.objects.first().id}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'app_pay/item_detail.html')


class TestBuyItem(CreateItem):
    """Дочерний класс. Модель тестирования страницы с покупкой товара"""

    def test_buy_detail_url_exists_at_desire_location(self):
        response = self.client.get(f'/buy/{Item.objects.first().id}/')
        self.assertEqual(response.status_code, 200)

    def test_buy_detail_shop_correct_template(self):
        response = self.client.get(reverse('buy', kwargs={'pk': Item.objects.first().id}))
        self.assertEqual(response.status_code, 200)
