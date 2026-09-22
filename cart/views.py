
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from products.models import Product
from django.contrib.auth.decorators import login_required

from .models import Cart, CartItem


@login_required
def add_to_cart(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    cart_item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if not created:

        cart_item.quantity += 1
        cart_item.save()

    return redirect('cart_detail')


@login_required
def cart_detail(request):

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    total = cart.total_price()

    return render(
        request,
        'cart/cart_detail.html',
        {
            'cart': cart,
            'items': items,
            'total': total,
        }
    )


@login_required
def update_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    if request.method == 'POST':

        quantity = int(
            request.POST.get('quantity', 1)
        )

        if quantity > 0:

            item.quantity = quantity
            item.save()

        else:

            item.delete()

    return redirect('cart_detail')


@login_required
def remove_from_cart(request, item_id):

    item = get_object_or_404(
        CartItem,
        id=item_id,
        cart__user=request.user
    )

    item.delete()

    return redirect('cart_detail')
@api_view(['GET'])
def cart_api(request):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    items = cart.items.all()

    cart_data = []

    for item in items:

        cart_data.append({
            'id': item.id,
            'product_id': item.product.id,
            'product_name': item.product.name,
            'price': str(item.product.price),
            'quantity': item.quantity,
            'subtotal': str(
                item.product.price * item.quantity
            )
        })

    total = sum(
        item.product.price * item.quantity
        for item in items
    )

    return Response({
        'cart_id': cart.id,
        'items': cart_data,
        'total_price': str(total)
    })
@api_view(['POST'])
def cart_add_api(request):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    product_id = request.data.get('product_id')
    quantity = request.data.get('quantity', 1)

    if not product_id:
        return Response(
            {'error': 'product_id is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    try:
        product = Product.objects.get(
            id=product_id
        )

    except Product.DoesNotExist:
        return Response(
            {'error': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    cart, created = Cart.objects.get_or_create(
        user=request.user
    )

    item, created = CartItem.objects.get_or_create(
        cart=cart,
        product=product
    )

    if created:
        item.quantity = quantity
    else:
        item.quantity += int(quantity)

    item.save()

    return Response({
        'message': 'Product added to cart',
        'product': product.name,
        'quantity': item.quantity
    }, status=status.HTTP_201_CREATED)
@api_view(['PUT'])
def cart_update_api(request, item_id):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        item = CartItem.objects.get(
            id=item_id,
            cart__user=request.user
        )

    except CartItem.DoesNotExist:
        return Response(
            {'error': 'Cart item not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    quantity = request.data.get('quantity')

    if not quantity:
        return Response(
            {'error': 'quantity is required'},
            status=status.HTTP_400_BAD_REQUEST
        )

    quantity = int(quantity)

    if quantity <= 0:
        return Response(
            {'error': 'Quantity must be greater than 0'},
            status=status.HTTP_400_BAD_REQUEST
        )

    item.quantity = quantity
    item.save()

    return Response({
        'message': 'Cart quantity updated',
        'item_id': item.id,
        'quantity': item.quantity
    })
@api_view(['DELETE'])
def cart_remove_api(request, item_id):

    if not request.user.is_authenticated:
        return Response(
            {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    try:
        item = CartItem.objects.get(
            id=item_id,
            cart__user=request.user
        )

    except CartItem.DoesNotExist:
        return Response(
            {'error': 'Cart item not found'},
            status=status.HTTP_404_NOT_FOUND
        )

    item.delete()

    return Response({
        'message': 'Product removed from cart'
    })
