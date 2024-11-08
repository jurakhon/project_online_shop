from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('productlist/', ProductListView.as_view(), name='product_list'),
    path("productdetail/<int:pk>", ProductDetailView.as_view(), name='product_detail'),
    path('productcreate/', ProductCreateView.as_view(), name='product_create'),
    path('productupdate/<int:pk>', ProductUpdateView.as_view(), name='product_update'),
    path('productdelete/<int:pk>', ProductDeleteView.as_view(), name='product_delete'),
    path('ordercreate/', OrderCreateView.as_view(), name='order_create'),
    path('orderupdate/<int:pk>', OrderUpdateView.as_view(), name='order_update'),
    path('orderdelete/<int:pk>', OrderDeleteView.as_view(), name='order_delete'),
    path('orderdetail/<int:pk>', OrderDetailView.as_view(), name='order_detail'),
    path('orderlist/', OrderListView.as_view(), name='order_list'),




]