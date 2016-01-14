from django.contrib.auth.models import User, Group
from app.models import Product
from rest_framework import routers, serializers, viewsets


class ProductSerializer(serializers.ModelSerializer):

    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = Product
        fields = ('id', 'owner', 'name', 'description', 'price', 'category', \
                'image')


# Serializers define the API representation.
class UserSerializer(serializers.HyperlinkedModelSerializer):

    products = serializers.PrimaryKeyRelatedField(many=True, \
            queryset=Product.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'products')

