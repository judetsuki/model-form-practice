from django.forms import ModelForm
from product_app.models import Product


class ProductForm(ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'description', 'price', 'stock', 'created_at']


form = ProductForm()
article = 