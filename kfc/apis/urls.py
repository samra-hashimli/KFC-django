from django.urls import path
from .views import ProductsAPIView, ProductDetailsAPIView, home


urlpatterns = [
    path(
        "products/",
        ProductsAPIView.as_view(),
        name="products"
    ),
    path(
        "products/<int:product_id>/",
        ProductDetailsAPIView.as_view(),
        name="product_id"
    ),
    path("", 
        home,
        name="home"
    ),
]
