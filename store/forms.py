from django import forms
from .models import Product, Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['product',]

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = '__all__'


