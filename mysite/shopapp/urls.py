
from django.urls import path
from .views import home_page, about_me, info_list, orders_list,  ProductDetailsView, product_list, ProductUpdateView

app_name = 'shopapp'

urlpatterns = [
    path("", home_page, name='home'),
    path('about/', about_me, name='about'),
    path('info/', info_list, name='info_list'),
    path('orders/', orders_list, name='orders_list'),
    path("products/", product_list, name='product_list'),
    path("products/<int:pk>/update/", ProductUpdateView.as_view(), name="product_update"),
    path("products/<int:pk>/", ProductDetailsView.as_view(), name="product_details"),

    ]