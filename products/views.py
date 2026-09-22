from django.shortcuts import render, get_object_or_404

from .models import Product, Category
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAdminUser
from .serializers import ProductSerializer
def product_list(request):

    category_id = request.GET.get('category')
    search_query = request.GET.get('search')

    products = Product.objects.all()
    categories = Category.objects.all()

    # Category filtering
    if category_id:
        products = products.filter(
            category_id=category_id
        )

    # Product search
    if search_query:
        products = products.filter(
            name__icontains=search_query
        )

    return render(
        request,
        'products/product_list.html',
        {
            'products': products,
            'categories': categories,
            'search_query': search_query,
        }
    )

def product_detail(request, product_id):

    product = get_object_or_404(
        Product,
        id=product_id
    )

    return render(
        request,
        'products/product_detail.html',
        {
            'product': product
        }
    )
@api_view(['GET', 'POST'])
def product_api(request):

    if request.method == 'GET':

        products = Product.objects.all()

        serializer = ProductSerializer(
            products,
            many=True
        )

        return Response(serializer.data)

    if request.method == 'POST':

        if not request.user.is_authenticated:
            return Response(
                {'error': 'Please login first'},
                status=status.HTTP_401_UNAUTHORIZED
            )

        if not request.user.is_staff:
            return Response(
                {'error': 'Only admin can create products'},
                status=status.HTTP_403_FORBIDDEN
            )

        serializer = ProductSerializer(
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(
                serializer.data,
                status=status.HTTP_201_CREATED
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET', 'PUT', 'DELETE'])

def product_detail_api(request, product_id):

    try:
        product = Product.objects.get(id=product_id)

    except Product.DoesNotExist:
        return Response(
            {'error': 'Product not found'},
            status=status.HTTP_404_NOT_FOUND
        )
    if request.method == 'PUT' or request.method == 'DELETE':
        if not request.user.is_authenticated:
            return Response( {'error': 'Please login first'},
            status=status.HTTP_401_UNAUTHORIZED
        )

    if not request.user.is_staff:
        return Response(
            {'error': 'Only admin can perform this operation'},
            status=status.HTTP_403_FORBIDDEN
        )

    # GET - Get one product
    if request.method == 'GET':

        serializer = ProductSerializer(product)

        return Response(serializer.data)

    # PUT - Update product
    elif request.method == 'PUT':

        serializer = ProductSerializer(
            product,
            data=request.data
        )

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    # DELETE - Delete product
    elif request.method == 'DELETE':

        product.delete()

        return Response(
            {'message': 'Product deleted successfully'},
            status=status.HTTP_200_OK
        )