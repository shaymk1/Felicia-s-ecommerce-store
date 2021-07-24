from django.shortcuts import render, get_object_or_404, redirect
from .models import Product  # , ReviewRating, ProductGallery
from category.models import Category
from carts.models import CartItem
from django.db.models import Q
from .models import *
from carts.views import _cart_id

from django.http import HttpResponse
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator


def home(request):
    products = Product.objects.all().filter(is_available=True)
    context = {

        'products': products
    }

    return render(request, 'store/home.html', context)


def store(request, category_slug=None):
    categories = None
    products = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        products = Product.objects.filter(
            category=categories, is_available=True)

        products = Product.objects.all().filter(is_available=True)
        product_count = products.count()
        paginator = Paginator(products, 1)  # how many products/page
        page = request.GET.get('page')  # give us the requested page number
        # paged products is the results of the 6 products /page requested from paginator
        paged_products = paginator.get_page(page)
        product_count = products.count()

    else:

        products = Product.objects.all().filter(is_available=True).order_by('id')
        product_count = products.count()
        paginator = Paginator(products, 6)  # how many products/page
        page = request.GET.get('page')  # give us the requested page number
        # paged products is the results of the 6 products /page requested from paginator
        paged_products = paginator.get_page(page)
        product_count = products.count()
    context = {



        # 'products': products, instead of passing products,we pass paged products
        'products': paged_products,
        'product_count ': product_count
    }

    return render(request, 'store/store.html', context)


def product_detail(request, category_slug, product_slug):
    try:
        single_product = Product.objects.get(
            category__slug=category_slug, slug=product_slug)  # category in store model and slug and category model we need access to

        in_cart = CartItem.objects.filter(
            cart__cart_id=_cart_id(request), product=single_product).exists()
        # return HttpResponse(in_cart)

    except Exception as e:
        raise e

    # if request.user.is_authenticated:
    #     try:
    #         orderproduct = OrderProduct.objects.filter(
    #             user=request.user, product_id=single_product.id).exists()
    #     except OrderProduct.DoesNotExist:
    #         orderproduct = None
    # else:
    #     orderproduct = None

    # # Get the reviews
    # reviews = ReviewRating.objects.filter(
    #     product_id=single_product.id, status=True)

    # # Get the product gallery
    # product_gallery = ProductGallery.objects.filter(
    #     product_id=single_product.id)

    context = {
        'single_product': single_product,
        'in_cart': in_cart,
        # 'orderproduct': orderproduct,
        # 'reviews': reviews,
        # 'product_gallery': product_gallery,
    }

    return render(request, 'store/product_detail.html', context)


def search(request):
    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            products = Product.objects.order_by('-created_date').filter(
                Q(description__icontains=keyword) |
                Q(product_name__icontains=keyword)
                # Q(category__icontains=keyword)

            )

            product_count = products.count()
    context = {
        'products': products,
        'product_count': product_count,
    }
    return render(request, 'store/store.html', context)


# def search(request):
#     if 'keyword 'in request.GET:
#         keyword = request.GET['keyword']
#         if keyword:
#             products = Product.objects.order_by('-created_date').filter(

#                 Q(description__icontains=keyword) |
#                 Q(product_name__icontains=keyword) |
#

#             )
#             product_count = products.count()
#     context = {

#         'products': products,
#         'product_count': product_count,
#     }
#     return render(request, 'store/store.html', context)
