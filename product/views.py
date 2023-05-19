from django.shortcuts import render
from .models import Product



# Create your views here.
def product_view(request):
    if request.method == 'GET':
        context = {
            'posts': Product.objects.all()
        }
        return render(request, 'posts/product.html', context=context)

def post_detail_view(request, id):
    if request.method == 'GET':
        post = Product.objects.get(id=id)

        context = {
            'post': post,
            'comment': post.comment_set.all()
        }

        return render(request, 'posts/detail.html', context=context)
