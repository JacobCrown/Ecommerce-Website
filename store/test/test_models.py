from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self):
        self.data1 = Category.objects.create(name='django', slug='django')

    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), 'django')


class TestProductModel(TestCase):
    def setUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create_user(username='bob')
        self.data1 = Product.objects.create(category_id=1,
            title="django beginners", created_by_id=1, slug='django-beginners', price=19.99, image='django')

    def test_products_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Product))

    def test_category_model_name(self):
        data = self.data1
        self.assertEqual(str(data), 'django beginners')
