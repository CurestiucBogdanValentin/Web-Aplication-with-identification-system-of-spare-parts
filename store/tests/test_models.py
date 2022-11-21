from django.test import TestCase
from django.contrib.auth.models import User
from store.models import Category, Product

class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data1=Category.objects.create(name='django', slug='django')
    def test_type_model_entry(self):
        ## tipul de data introdusa
        data=self.data1
        self.assertTrue(isinstance(data,Category))
    def test_category_model_entry(self):
        ## category defaulth name

        data=self.data1
        self.assertEqual(str(data),'django')

class TestProductModel(TestCase):
    def SetUp(self):
        Category.objects.create(name='django', slug='django')
        User.objects.create(username='admin')
        self.data1=Product.objects.create(category_p_id=1, name_part='piesa django', created_by_id=1, slug='django-website',price='20.00',image='django')

    def test_products_model_entry(self):
       data=self.data1
       self.assertTrue(isinstance(data,Product))
       self.assertEqual(str(data),'piesa django')  