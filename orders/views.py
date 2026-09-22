from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect, render

from cart.models import Cart
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Order,OrderItem
from .serializers import OrderSerializer

from cart.models import Cart
@login_required
def checkout(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.select_related('product').all()

    if not items:
        return redirect('cart_detail')

    total = cart.total_price()

    if request.method == 'POST':

        # Create Order
        order = Order.objects.create(
            user=request.user,
            total_amount=total,
            status='Pending'
        )

        # Create Order Items
        for item in items:

            OrderItem.objects.create(
                order=order,
                product=item.product,
                quantity=item.quantity,
                price=item.product.price
            )

        # Clear Cart
        items.delete()

        # Go to confirmation page
        return redirect(
            'order_confirmation',
            order_id=order.id
        )

    return render(
        request,
        'orders/checkout.html',
        {
            'cart': cart,
            'items': items,
            'total': total,
        }
    )
@login_required
def order_confirmation(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    return render(
        request,
        'orders/order_confirmation.html',
        {
            'order': order,
        }
    )
@login_required
def my_orders(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'orders/my_orders.html',
        {
            'orders': orders,
        }
    )
@login_required
def order_detail(request, order_id):

    order = get_object_or_404(
        Order,
        id=order_id,
        user=request.user
    )

    items = order.items.select_related('product').all()

    return render(
        request,
        'orders/order_detail.html',
        {
            'order': order,
            'items': items,
        }
    )
@api_view(['GET'])
def order_api(request):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    serializer = OrderSerializer(
        orders,
        many=True
    )

    return Response(
        serializer.data
    )
@api_view(['GET'])
def order_detail_api(request, order_id):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:

        order = Order.objects.get(
            id=order_id,
            user=request.user
        )

    except Order.DoesNotExist:

        return Response(
            {'error': 'Order not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    serializer = OrderSerializer(order)

    return Response(
        serializer.data
    )
@api_view(['POST'])
def checkout_api(request):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:

        cart = Cart.objects.get(
            user=request.user
        )

    except Cart.DoesNotExist:

        return Response(
            {'error': 'Cart is empty'},
            status=status.HTTP_400_BAD_REQUEST
        )

    cart_items = cart.items.all()

    if not cart_items.exists():

        return Response(
            {'error': 'Cart is empty'},
            status=status.HTTP_400_BAD_REQUEST
        )

    total_amount = sum(
        item.product.price * item.quantity
        for item in cart_items
    )

    order = Order.objects.create(
        user=request.user,
        total_amount=total_amount,
        status='Pending'
    )

    for item in cart_items:

        order.items.create(
            product=item.product,
            quantity=item.quantity,
            price=item.product.price
        )

    cart_items.delete()

    serializer = OrderSerializer(order)

    return Response(
        serializer.data,
        status=status.HTTP_201_CREATED
    )