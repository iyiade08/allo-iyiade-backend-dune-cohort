from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Product, Category
from .serializers import ProductSerializer, CategorySerializer


# ─── Product API Views ───────────────────────────────────────

@api_view(['GET', 'POST'])
def product_list_api(request):

    # GET — return all products
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)

    # POST — create a new product
    if request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def product_detail_api(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'},
                       status=status.HTTP_404_NOT_FOUND)

    # GET — return one product
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    # PUT — update a product
    if request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # DELETE — delete a product
    if request.method == 'DELETE':
        product.delete()
        return Response({'message': 'Product deleted successfully'},
                       status=status.HTTP_204_NO_CONTENT)


# ─── Category API Views ───────────────────────────────────────

@api_view(['GET'])
def category_list_api(request):
    categories = Category.objects.all()
    serializer = CategorySerializer(categories, many=True)
    return Response(serializer.data)