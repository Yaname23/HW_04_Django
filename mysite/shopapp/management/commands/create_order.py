from typing import Sequence

from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Product, Order, Client


class Command(BaseCommand):
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Create order with products')
        client = Client.objects.get()
        order, created = Order.objects.get_or_create(
            client=client
        )

        self.stdout.write(f'Create order {order}')



    # @transaction.atomic
    # def handle(self, *args, **options):
    #     self.stdout.write('Create order with products')
    #     products: Sequence[Product] = Product.objects.defer("desctiption", "price", "quantity", "created_at").all()
    #     sum_order= Product.objects.annotate(sum_order=Sum('price'))
    #     # Author.objects.annotate(total_pages=Sum('book__pages'))
    #
    #     order, created = Order.objects.get_or_create()
    #
    #     for product in products:
    #         order.products.add(product)
    #     order.save()
    #     self.stdout.write(f'Create order - {order}')