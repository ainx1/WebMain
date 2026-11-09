from django.test import TestCase
from rest_framework.test import APIClient
from model_bakery import baker
from PCShop.models import Category, Manufacturer, Component, Order, OrderItem, PcBuild
# Create your tests here.
# 1) Категория
class CategoryViewsetTestCase(TestCase):
    
    def setUp(self):
        self.client = APIClient()
    
    # Тест на запрос списка данных
    def test_get_list(self):
        category = baker.make('PCShop.Category')

        r = self.client.get('/api/categories/')
        data = r.json()
        print(data)

        assert category.name == data[0]['name']
        assert category.id == data[0]['id']
        assert len(data) == 1

    # Тест на создание записи
    def test_create_category(self):

        r = self.client.post('/api/categories/', {
            'name': 'CPU', 
        })

        new_category_id = r.json()['id']
        categories = Category.objects.all()
        assert len(categories) == 1

        new_category = Category.objects.filter(id=new_category_id).first()
        assert new_category.name == 'CPU'

    # Тест на удаление данных
    def test_delete_category(self):
        categories = baker.make('PCShop.Category', 10)

        r = self.client.get('/api/categories/')
        data = r.json()
        assert len(data) == 10

        category_id_to_delete = categories[3].id
        self.client.delete(f'/api/categories/{category_id_to_delete}/')

        r = self.client.get('/api/categories/')
        data = r.json()
        assert len(data) == 9

        assert category_id_to_delete not in [i['id'] for i in data]

    # Тест на обновление данных
    def test_update_category(self):
        categories = baker.make('PCShop.Category', 10)
        category: Category = categories[2]

        r = self.client.get(f'/api/categories/{category.id}/')
        data = r.json()
        assert data['name'] == category.name

        r = self.client.put(f'/api/categories/{category.id}/', {
            'name': 'CPU'
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/categories/{category.id}/')
        data = r.json()
        assert data['name'] == 'CPU'

        category.refresh_from_db()
        assert data['name'] == category.name

# 2) Производитель
class ManufacturerViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Тест на запрос списка данных
    def test_get_list(self):
        manufacturer = baker.make('PCShop.Manufacturer')

        r = self.client.get('/api/manufacturers/')
        data = r.json()
        print(data)

        assert manufacturer.name == data[0]['name']
        assert manufacturer.id == data[0]['id']
        assert len(data) == 1

    # Тест на создание записи
    def test_create_manufacturer(self):
        r = self.client.post('/api/manufacturers/', {
            'name': 'ASUS',
            'country': 'Тайвань'
        })

        new_manufacturer_id = r.json()['id']
        manufacturers = Manufacturer.objects.all()
        assert len(manufacturers) == 1

        new_manufacturer = Manufacturer.objects.filter(id=new_manufacturer_id).first()
        assert new_manufacturer.name == 'ASUS'
        assert new_manufacturer.country == 'Тайвань'

    # Тест на удаление данных
    def test_delete_manufacturer(self):
        manufacturers = baker.make('PCShop.Manufacturer', 10)

        r = self.client.get('/api/manufacturers/')
        data = r.json()
        assert len(data) == 10

        manufacturer_id_to_delete = manufacturers[3].id
        self.client.delete(f'/api/manufacturers/{manufacturer_id_to_delete}/')

        r = self.client.get('/api/manufacturers/')
        data = r.json()
        assert len(data) == 9

        assert manufacturer_id_to_delete not in [i['id'] for i in data]

    # Тест на обновление данных
    def test_update_manufacturer(self):
        manufacturers = baker.make('PCShop.Manufacturer', 10)
        manufacturer: Manufacturer = manufacturers[2]

        r = self.client.get(f'/api/manufacturers/{manufacturer.id}/')
        data = r.json()
        assert data['name'] == manufacturer.name

        r = self.client.put(f'/api/manufacturers/{manufacturer.id}/', {
            'name': 'Intel'
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/manufacturers/{manufacturer.id}/')
        data = r.json()
        assert data['name'] == 'Intel'

        manufacturer.refresh_from_db()
        assert data['name'] == manufacturer.name


# 3) Комплектующее
class ComponentViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Тест на запрос списка данных
    def test_get_list(self):
        cat = baker.make('PCShop.Category')
        manuf = baker.make('PCShop.Manufacturer')
        component = baker.make('PCShop.Component', category=cat, manufacturer=manuf)

        r = self.client.get('/api/components/')
        data = r.json()
        print(data)

        assert component.name == data[0]['name']
        assert component.id == data[0]['id']
        assert component.category.id == data[0]['category']['id']
        assert component.manufacturer.id == data[0]['manufacturer']['id']
        assert len(data) == 1

    # Тест на создание записи
    def test_create_component(self):
        r = self.client.post('/api/components/', {
            'name': 'RTX 4070',
            'price': 65000,
            'stock': 5
        })

        new_component_id = r.json()['id']
        components = Component.objects.all()
        assert len(components) == 1

        new_component = Component.objects.filter(id=new_component_id).first()
        assert new_component.name == 'RTX 4070'
        assert new_component.price == 65000

    # Тест на удаление данных
    def test_delete_component(self):
        components = baker.make('PCShop.Component', 10)

        r = self.client.get('/api/components/')
        data = r.json()
        assert len(data) == 10

        component_id_to_delete = components[3].id
        self.client.delete(f'/api/components/{component_id_to_delete}/')

        r = self.client.get('/api/components/')
        data = r.json()
        assert len(data) == 9

        assert component_id_to_delete not in [i['id'] for i in data]

    # Тест на обновление данных
    def test_update_component(self):
        components = baker.make('PCShop.Component', 10)
        component: Component = components[2]

        r = self.client.get(f'/api/components/{component.id}/')
        data = r.json()
        assert data['name'] == component.name

        r = self.client.put(f'/api/components/{component.id}/', {
            'name': 'Core i5-14600K'
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/components/{component.id}/')
        data = r.json()
        assert data['name'] == 'Core i5-14600K'

        component.refresh_from_db()
        assert data['name'] == component.name


# 4) Заказ
class OrderViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Тест на запрос списка данных
    def test_get_list(self):
        order = baker.make('PCShop.Order')

        r = self.client.get('/api/orders/')
        data = r.json()
        print(data)

        assert order.customer_name == data[0]['customer_name']
        assert order.id == data[0]['id']
        assert len(data) == 1

    # Тест на создание записи
    def test_create_order(self):
        r = self.client.post('/api/orders/', {
            'customer_name': 'Иван Иванов',
            'customer_phone': '+79990001122',
            'status': 'Новый'
        })

        new_order_id = r.json()['id']
        orders = Order.objects.all()
        assert len(orders) == 1

        new_order = Order.objects.filter(id=new_order_id).first()
        assert new_order.customer_name == 'Иван Иванов'

    # Тест на удаление данных
    def test_delete_order(self):
        orders = baker.make('PCShop.Order', 10)

        r = self.client.get('/api/orders/')
        data = r.json()
        assert len(data) == 10

        order_id_to_delete = orders[3].id
        self.client.delete(f'/api/orders/{order_id_to_delete}/')

        r = self.client.get('/api/orders/')
        data = r.json()
        assert len(data) == 9

        assert order_id_to_delete not in [i['id'] for i in data]

    # Тест на обновление данных
    def test_update_order(self):
        orders = baker.make('PCShop.Order', 10)
        order: Order = orders[2]

        r = self.client.get(f'/api/orders/{order.id}/')
        data = r.json()
        assert data['customer_name'] == order.customer_name

        r = self.client.put(f'/api/orders/{order.id}/', {
            'customer_name': 'Петр Петров'
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/orders/{order.id}/')
        data = r.json()
        assert data['customer_name'] == 'Петр Петров'

        order.refresh_from_db()
        assert data['customer_name'] == order.customer_name


# 5) Комплектующее в заказе
class OrderItemViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Тест на запрос списка данных
    def test_get_list(self):
        ord_obj = baker.make('PCShop.Order')
        comp = baker.make('PCShop.Component')
        order_item = baker.make('PCShop.OrderItem', order=ord_obj, product=comp)

        r = self.client.get('/api/order-items/')
        data = r.json()
        print(data)

        assert order_item.id == data[0]['id']
        assert order_item.order.id == data[0]['order']['id']
        assert order_item.product.id == data[0]['product']['id']
        assert len(data) == 1

    # Тест на создание записи
    def test_create_order_item(self):
        r = self.client.post('/api/order-items/', {
            'quantity': 2,
            'price': 50000
        })

        new_item_id = r.json()['id']
        order_items = OrderItem.objects.all()
        assert len(order_items) == 1

        new_item = OrderItem.objects.filter(id=new_item_id).first()
        assert new_item.quantity == 2
        assert new_item.price == 50000

    # Тест на удаление данных
    def test_delete_order_item(self):
        order_items = baker.make('PCShop.OrderItem', 10)

        r = self.client.get('/api/order-items/')
        data = r.json()
        assert len(data) == 10

        item_id_to_delete = order_items[3].id
        self.client.delete(f'/api/order-items/{item_id_to_delete}/')

        r = self.client.get('/api/order-items/')
        data = r.json()
        assert len(data) == 9

        assert item_id_to_delete not in [i['id'] for i in data]

    # Тест на обновление данных
    def test_update_order_item(self):
        order_items = baker.make('PCShop.OrderItem', 10)
        order_item: OrderItem = order_items[2]

        r = self.client.get(f'/api/order-items/{order_item.id}/')
        data = r.json()
        assert data['quantity'] == order_item.quantity

        r = self.client.put(f'/api/order-items/{order_item.id}/', {
            'quantity': 5
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/order-items/{order_item.id}/')
        data = r.json()
        assert data['quantity'] == 5

        order_item.refresh_from_db()
        assert data['quantity'] == order_item.quantity


# 6) Шаблон сборки ПК
class PcBuildViewsetTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    # Тест на запрос списка данных
    def test_get_list(self):
        pc_build = baker.make('PCShop.PcBuild')

        r = self.client.get('/api/pc-builds/')
        data = r.json()
        print(data)

        assert pc_build.name == data[0]['name']
        assert pc_build.id == data[0]['id']
        assert len(data) == 1

    # Тест на создание записи
    def test_create_pc_build(self):
        r = self.client.post('/api/pc-builds/', {
            'name': 'Игровой ПК'
        })

        new_build_id = r.json()['id']
        pc_builds = PcBuild.objects.all()
        assert len(pc_builds) == 1

        new_build = PcBuild.objects.filter(id=new_build_id).first()
        assert new_build.name == 'Игровой ПК'

    # Тест на удаление данных
    def test_delete_pc_build(self):
        pc_builds = baker.make('PCShop.PcBuild', 10)

        r = self.client.get('/api/pc-builds/')
        data = r.json()
        assert len(data) == 10

        build_id_to_delete = pc_builds[3].id
        self.client.delete(f'/api/pc-builds/{build_id_to_delete}/')

        r = self.client.get('/api/pc-builds/')
        data = r.json()
        assert len(data) == 9

        assert build_id_to_delete not in [i['id'] for i in data]

    # Тест на обновление данных
    def test_update_pc_build(self):
        pc_builds = baker.make('PCShop.PcBuild', 10)
        pc_build: PcBuild = pc_builds[2]

        r = self.client.get(f'/api/pc-builds/{pc_build.id}/')
        data = r.json()
        assert data['name'] == pc_build.name

        r = self.client.put(f'/api/pc-builds/{pc_build.id}/', {
            'name': 'Офисный ПК'
        })
        assert r.status_code == 200

        r = self.client.get(f'/api/pc-builds/{pc_build.id}/')
        data = r.json()
        assert data['name'] == 'Офисный ПК'

        pc_build.refresh_from_db()
        assert data['name'] == pc_build.name