from django.urls import path
from .views import (
    product_detail_view, 
    render_initial_data,
    dynamic_lookup_view,
    product_delete_view,
    product_list_view
    )

app_name = 'products'

urlpatterns = [
    path('', product_list_view, name='product-detail'),
    path('product/', product_detail_view, name='detail'),
    path('<int:id>/', dynamic_lookup_view, name='single-product'),
    path('<int:id>/delete/', product_delete_view, name='product-delete'),
    path('create/', render_initial_data, name='create'),
]