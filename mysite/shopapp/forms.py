
from django.forms import forms, ModelForm
from django.urls import reverse, reverse_lazy

from shopapp.models import Product, Order, Client, ProductImage


class ProductForm(ModelForm):

    class Meta:
       model = Product
       # fields = ["picture", "name", "price", "description", "quantity", "created_at", "pk"]
       fields = '__all__'

class OrderForm(forms.Form):

    class Meta:
       model = Order
       fields = "client", "products", "final_price", "created_at",

class ClientForm(forms.Form):

    class Meta:
       model = Client
       fields = "name", "email", "phone", "address", "registration_date"

