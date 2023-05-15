from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from .models import Product


# Create your views here.
def product_view(request):
    if request.method == 'GET':
        context = {
            'posts': Product.objects.all()
        }
        return render(request, 'product/product.html', context=context)
