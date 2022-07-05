from django.shortcuts import render, get_object_or_404
from .models import Product,Category
from django.http import JsonResponse
from django.core.paginator import Paginator
# <!--*****************************CART ******************************-->
from cart.form import CartAddProductForm
# <!--*****************************CART ******************************-->
# Create your views here.


def product_list(request):
    product_list = Product.objects.all()
    category = Category.objects.all()
    paginator = Paginator(product_list, 2)
    page_number = request.GET.get('page')
    product_list = paginator.get_page(page_number)
    context ={
        'products': product_list,
        'category':category
    }
    return render(request,'product_list.html',context)



def product_detail(request,slug):
    # product_detail = Product.objects.get(PRDSlug=slug)
    product_detail = get_object_or_404(Product,PRDSlug=slug)
    cart_product_form = CartAddProductForm()
    context = {
        'product_detail': product_detail,
        'cart_product_form':cart_product_form
    }
    return render(request,'product_detail.html',context)


def category_detail(request, slug):
    category = get_object_or_404(Category, CATSlug=slug)
    # category = Category.objects.filter(CATSlug=slug)
    products = category.products.filter(PRDparent=None)

    context = {
        'category': category,
        'products': products
    }

    return render(request, 'product_list.html', context)

def search(request):
    q=request.GET['q']
    data=Product.objects.filter(PRDName__icontains=q).order_by('-id')
    return render(request,'search.html',{'data':data})







