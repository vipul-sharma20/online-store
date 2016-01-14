from django.shortcuts import render
from django.contrib.auth.models import User, Group
from django.http import HttpResponse

from app.models import Product
from app.serializers import ProductSerializer, UserSerializer

from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view, permission_classes
from rest_framework import viewsets, status, permissions, generics


class ProductList(generics.ListCreateAPIView):
    """
    List all products, or create a new product.
    """

    permission_classes = (permissions.IsAuthenticated,)

    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

    def get_queryset(self):

        queryset = Product.objects.all()
        q = self.request.query_params.get('q', '')

        queryset = queryset.filter(name__icontains=q)
        return queryset


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((permissions.IsAuthenticated,))
def product_detail(request, pk):
    """
    Retrieve, update or delete a product instance.
    """

    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)

    elif request.method == 'PUT':
        if product.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            serializer = ProductSerializer(product, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        if product.owner != request.user:
            return Response(status=status.HTTP_403_FORBIDDEN)
        else:
            product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
