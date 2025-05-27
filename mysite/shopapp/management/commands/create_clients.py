from django.core.management import BaseCommand
from django.db import transaction

from shopapp.models import Client


class Command(BaseCommand):
    """Creates products """
    def handle(self, *args, **options):
        self.stdout.write('Create client')
        client, created = Client.objects.get_or_create(
            name="Иванов Иван",
            email="Ivanco@mail.com",
            phone="89123456789",
            address="г.Мира, ул.Победы,5",

        )

        client.save()
        self.stdout.write(f'Create client - {client.name}')

