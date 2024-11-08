

from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.http import HttpResponse
from django.urls import reverse, reverse_lazy
from django.views import View
from django.views.generic import ListView, TemplateView, DetailView, CreateView, UpdateView, DeleteView

from .models import *
from .forms import *


# Create your views here.

class HomeView(TemplateView):
    template_name = "home.html"
    context_object_name = 'home'

class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    context_object_name = "product_list"

class ProductDetailView(DetailView):
    model = Product
    template_name = "product_detail.html"
    context_object_name = "product_detail"

class ProductCreateView(CreateView):
    model = Product
    template_name = "product_create.html"
    fields = '__all__'
    success_url = reverse_lazy("product_list")

class ProductUpdateView(UpdateView):
    model = Product
    fields = '__all__'
    success_url = reverse_lazy("product_list")
    template_name = "product_create.html"

class ProductDeleteView(DeleteView):
    model = Product
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("product_list")


class OrderCreateView(CreateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy("home")
    template_name = "order_create.html"


class OrderDetailView(DetailView):
    model = Order
    template_name = "order_detail.html"
    context_object_name = "order_detail"

class OrderUpdateView(UpdateView):
    model = Order
    fields = '__all__'
    success_url = reverse_lazy("home")
    template_name = "order_update.html"

class OrderDeleteView(DeleteView):
    model = Order
    template_name = "confirm_delete.html"
    success_url = reverse_lazy("home")

class OrderListView(ListView):
    model = Order
    template_name = "order_list.html"
    context_object_name = "order_list"


def order_create(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    if request.method == "POST":
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.product = product
            order.price = product.price  # Set the price from the product
            order.save()
            return redirect('order_confirmation')
    else:
        form = OrderForm()
    return render(request, 'order_create.html', {'form': form, 'product': product})

