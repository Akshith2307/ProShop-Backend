from django.shortcuts import render
from django.http import JsonResponse
from .models import Product
from .p import products
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer  import ProductSerializer 

@api_view(['GET'])
def getRoutes(request):
    routes = [
        '/api/products/',
    ]
    return Response(routes)
@api_view(['GET'])
def getProducts (request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def getProduct (request, pk):
    products = Product.objects.get(_id=pk)
    serializer = ProductSerializer(products, many=False)
    return Response(serializer.data)

