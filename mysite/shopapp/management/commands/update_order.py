from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Product, Order, Client

class Command(BaseCommand):

    def handle(self, *args, **options):

        order = Order.objects.first()
        if not order:
            self.stdout.write('No order found')
            return
        products = Product.objects.all()

        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(f'Successfully added products {order.products.all()} to order {{order}}')
