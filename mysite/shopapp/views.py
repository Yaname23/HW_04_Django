
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpRequest
from django.urls import reverse
from django.views.generic import UpdateView, DetailView

from .forms import ProductForm
from .models import Order, Product, ProductImage


def home_page(request):
    context = {

    }
    return render(request, 'shopapp/home.html', context=context)

def about_me(request):
    context = {

    }
    return render(request, 'shopapp/about-me.html', context=context)


def info_list(request):
    inf = Order.objects.all()

    context = {
        "inf": inf,
        "orders": Order.objects.select_related('client').prefetch_related('products').all(),
    }

    return render(request, 'shopapp/info_list.html', context=context)

def orders_list(request: HttpRequest):
    context = {
        "orders": Order.objects.select_related('client').prefetch_related('products').all(),
    }
    return render(request, 'shopapp/orders_list.html', context=context)

def product_list(request):
    context = {
        "products": Product.objects.all(),
    }
    return render(request, 'shopapp/product_list.html', context=context)
class ProductDetailsView(DetailView):
    template_name = "shopapp/product_details.html"
    queryset = Product.objects.prefetch_related("images")
    context_object_name = "product"


class ProductUpdateView(UpdateView):
    model = Product

    template_name_suffix = "_update_form"
    form_class = ProductForm


    def get_success_url(self):
        products = Product.objects.all()
        for product in products:
            return reverse('shopapp:product_details',kwargs={"pk":product.pk})
    def form_valid(self, form):
        response = super().form_valid(form)
        for image in form.files.getlist("images"):
            ProductImage.objects.create(
                product=self.object,
                image=image,
            )
        return response

