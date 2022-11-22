from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from app_pay.models import Item

TEST_ITEM_RECORDS = 2


class Command(BaseCommand):
    help = f'Добавление {TEST_ITEM_RECORDS} записей истории'

    def handle(self, *args, **kwargs):
        for i in range(1, TEST_ITEM_RECORDS+1):
            Item.objects.create(name=f'product {i}',
                                description=f'description {i}',
                                price=1000*(i+1))
        self.stdout.write('Товары успешно загружены')
