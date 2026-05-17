from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer
from .filters import ProductFilter


class ProductPagination(PageNumberPagination):
    page_size = 6


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_list_api(request):

    if request.method == 'GET':
        products = Product.objects.all()

        # Filtering
        filterset = ProductFilter(request.GET, queryset=products)
        products = filterset.qs

        # Search by name
        search = request.GET.get('search')
        if search:
            products = products.filter(name__icontains=search)

        # Ordering by price
        ordering = request.GET.get('ordering')
        if ordering in ['price', '-price']:
            products = products.order_by(ordering)

        # Pagination
        paginator = ProductPagination()
        result_page = paginator.paginate_queryset(products, request)
        serializer = ProductSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)

    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(created_by=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticatedOrReadOnly])
def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'},
                       status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    if request.method == 'PUT':
        if product.created_by != request.user and not request.user.is_staff:
            return Response(
                {'error': 'You do not have permission to edit this product.'},
                status=status.HTTP_403_FORBIDDEN
            )
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        if product.created_by != request.user:
            return Response(
                {'error': 'You do not have permission to delete this product.'},
                status=status.HTTP_403_FORBIDDEN
            )
        product.delete()
        return Response({'message': 'Product deleted successfully'},
                       status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)