from django.shortcuts import render
from .form import OrderCreateForm
from .models import OrderItem,Order
from cart.cart import Cart



def order_create(request):
    cart = Cart(request)
    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save()
            for item in cart:
                OrderItem.objects.create(
                    order=order,
                    created_by=request.user,
                    product=item['product'],
                    price=item['price'],
                    quantity=item['quantity'])
            cart.clear()
            context = {
                'order':order
            }
            return render(request,'order/created.html',context)
    else:
        form = OrderCreateForm()
    context = {
        'cart':cart,
        'form':form
    }
    return render(request,'order/create.html',context)


def my_order(request):
    created_by = request.user
    orders = OrderItem.objects.filter(created_by=created_by)

    context = {
        'orders': orders,
    }
    return render(request,'order/my_order.html',context)