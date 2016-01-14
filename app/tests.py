from django.test import TestCase, Client
from django.contrib.auth.models import User

from app.views import product_detail, ProductList
from app.models import Product

from rest_framework import status
from rest_framework.test import APIRequestFactory, APIClient, force_authenticate
import json
from collections import OrderedDict

class ProductTest(TestCase):

    fixtures = ['test_users.json', 'test_products.json']

    def test_get_product_no_auth(self):

        client = APIClient()
        response = self.client.get('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, \
                {"detail":"Authentication credentials were not provided."})

    def test_get_product_with_auth(self):

        c = APIClient()
        c.login(username='bruce', password='testpass')
        response = c.get('/products/1/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.content, '{"id":1,"owner":"bruce","name":"Bat Mobile","description":"Black Batmobile","price":200,"category":"Automobile","image":""}')

    def test_post_product_no_auth(self):

        client = APIClient()
        data = {'name': 'Wayne Manor', 'price': 500, 'owner':1}
        response = client.post('/products/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, \
                {"detail":"Authentication credentials were not provided."})

    def test_post_product_with_auth(self):
        client = APIClient()
        client.login(username='bruce', password='testpass')
        data = {'name': 'Wayne Manor', 'price': 500, 'owner':1}
        response = client.post('/products/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Product.objects.count(), 2)

    def test_put_product_no_auth(self):

        client = APIClient()
        data = {'name': "Bane's mask", 'price': 500, 'owner':1}
        response = client.post('/products/1/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, \
                {"detail":"Authentication credentials were not provided."})

    def test_put_product_with_auth(self):
        client = APIClient()
        client.login(username='bruce', password='testpass')
        data = {'name': "Bane's mask", 'price': 500, 'owner':1}
        response = client.put('/products/1/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Product.objects.count(), 1)

    def test_delete_product_no_auth(self):

        client = APIClient()
        response = client.delete('/products/1/')

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        self.assertEqual(response.data, \
                {"detail":"Authentication credentials were not provided."})

    def test_delete_product_with_auth(self):

        client = APIClient()
        client.login(username='bruce', password='testpass')
        response = client.delete('/products/1/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Product.objects.count(), 0)

