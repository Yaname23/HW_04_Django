# Generated by Django 5.2.1 on 2025-05-22 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0004_orderitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='client',
        ),
        migrations.AlterField(
            model_name='order',
            name='products',
            field=models.ManyToManyField(related_name='products', to='shopapp.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='client',
            field=models.ManyToManyField(related_name='client', to='shopapp.client'),
        ),
    ]
