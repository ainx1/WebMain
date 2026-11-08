from django.test import TestCase
from rest_framework.test import APIClient
from model_bakery import baker
from PCShop.models import Category, Manufacturer, Component, Order, OrderItem, PcBuild
# Create your tests here.
class CategoryViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
    
    def test_get_list(self):
        category = baker.make('PCShop.Category')

        r = self.client.get('/api/categories/')
        data = r.json()
        print(data)

        assert category.name == data[0]['name']
        assert category.id == data[0]['id']
        assert len(data) == 1


    def test_create_category(self):

        r = self.client.post('/api/categories/', {
            'name': 'CPU', 
        })

        new_category_id = r.json()['id']
        categories = Category.objects.all()
        assert len(categories) == 1

        new_category = Category.objects.filter(id=new_category_id).first()
        assert new_category.name == 'CPU'


