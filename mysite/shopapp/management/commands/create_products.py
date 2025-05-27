from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """Creates products """
    def handle(self, *args, **options):
        self.stdout.write('Create product')

        product, created = Product.objects.get_or_create(
            name="Кофе",
            description="90 гр.",
            price=444,
            quantity=43,

        )

        product.save()
        self.stdout.write(f'Create client - {product.name}, {product.description} ')
