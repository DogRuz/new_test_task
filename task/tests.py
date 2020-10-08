from django.test import TestCase

from task.models import Product

import json


class ViewsTestCase(TestCase):
    def test_get_list_categories(self):
        response = self.client.get('/api/get_list_categories/')
        self.assertEqual(response.status_code, 200)

    def test_insert_product(self):
        response = self.client.post('/api/insert_product',
                                    {'title': 'Hit', 'description': "peanut candy", 'is_active': True})
        self.assertEqual(response.status_code, 200)

    def test_get_product_detail_card(self):
        Product.objects.create(title="Hit", description="peanut candy", is_active=True)
        response = self.client.get('/api/get_product_detail_card/{}'.format(1))
        bd_product = Product.objects.filter(id=1).values('id', 'description', 'title', 'category__title',
                                                         'company__description', 'is_active')
        self.assertQuerysetEqual(response.data, map(repr, bd_product))

    def test_delete_changes_product(self):
        Product.objects.create(title="Hit", description="peanut candy", is_active=True)
        response = self.client.delete('/api/changes_product/1')
        self.assertEqual(response.status_code, 200)
