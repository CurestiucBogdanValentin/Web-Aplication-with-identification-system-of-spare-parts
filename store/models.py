from enum import unique
from http.client import CREATED
from sre_parse import CATEGORIES
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active=True)
        
class Category(models.Model):
   id=models.AutoField(primary_key=True, serialize=False)
   name= models.CharField(max_length=255, db_index=True)
   slug = models.SlugField(max_length=500, unique= True) 
   
   class Meta:
      verbose_name_plural='categories'
   
   def __str__(self):
      return self.name

   def get_absolute_url(self): 
      return reverse('store:category_list', args=[self.slug])

class Product(models.Model):
  
   category_p=models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE) ## 
   created_by=models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
   part_number=models.IntegerField()
   name_part=models.CharField(max_length=500)
   code=models.CharField(max_length=500)  ## de pe schema de motaj a piesei\
   quantity=models.IntegerField()
   image= models.ImageField(upload_to='images/')
   slug=models.SlugField(max_length=250)
   price=models.DecimalField(max_digits=5, decimal_places=2)
   in_stock=models.BooleanField(default=True)
   is_active=models.BooleanField(default=True)
   created = models.DateTimeField(auto_now_add=True)
   updated = models.DateTimeField(auto_now=True)
   objects = models.Manager()
   products = ProductManager()
   brand=models.CharField(max_length=5000)

   class Meta:
      verbose_name_plural='Products'
      ordering=('-created',)
   
   def get_absolute_url(self):  ##aici am creat functia dolosita pentru a face link uri dinamice pentru produse
      return reverse('store:product_detail',args=[self.slug])


   def __str__(self):
      return self.name_part