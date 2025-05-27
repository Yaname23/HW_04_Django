from django.db import models

def product_preview_directory_path(instance: "Product", filename: str) -> str:

    return "products/product_{pk}/picture/{filename}".format(

        pk=instance.pk,
        filename=filename,
    )

class Client(models.Model):
    name = models.CharField(max_length=100, db_index=True)
    email = models.EmailField()
    phone = models.DecimalField(default=0, max_digits=12, decimal_places=0)
    address = models.TextField(null=False, blank=True)
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return f'{self.name}/n{self.email}/n{self.phone}/n{self.address}/n{self.registration_date}'

class Product(models.Model):
    class Meta:
        ordering = ['name', 'price']

    name = models.CharField(max_length=100, db_index=True)
    description = models.TextField(null=False, blank=True, db_index=True)
    price = models.DecimalField(default=0, max_digits=8, decimal_places=2)
    quantity = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    picture = models.ImageField(null=True, blank=True, upload_to=product_preview_directory_path)

    def __str__(self):
        return f'{self.name}/n{self.description}/n{self.price}/n{self.quantity}/n{self.created_at}'

def product_images_directory_path(instance: "ProductImage",filename: str) -> str:
    return "products/product_{pk}/image/{filename}".format(
        pk=instance.product.pk,
        filename=filename,
    )

class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=product_images_directory_path)
    description = models.CharField(max_length=200, null=False, blank=True)

class Order(models.Model):

    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупатель')
    clients = models.ManyToManyField(Client, blank=True, related_name='orders')
    products = models.ManyToManyField('Product', blank=True, related_name='orders')
    final_price = models.DecimalField(default=1, max_digits=20, decimal_places=2)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('-created_at', 'client')

class OrderItem(models.Model):
    """ Предмет заказа """
    client = models.ForeignKey(Client, on_delete=models.CASCADE, verbose_name='Покупатель')
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1, blank=True)
    final_price = models.IntegerField(verbose_name='Общая цена', blank=True)

    def save(self, *args, **kwargs):
        self.final_price = self.quantity * self.product.price
        super().save(*args, **kwargs)

    def __str__(self):
        return "Объект: {} (заказ)".format(self.product.name)

    class Meta:
        verbose_name = 'Объект заказа'
        verbose_name_plural = 'Объекты заказа'



