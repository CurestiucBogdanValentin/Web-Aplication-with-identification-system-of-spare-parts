from http.client import HTTPResponse
from django.conf import settings
from django.shortcuts import render
from matplotlib.style import context
from django.core.files.storage import FileSystemStorage
import sys
from keras.models import load_model
from PIL import Image, ImageOps
import numpy as np
import os, os.path 
from .models import Category, Product
from django.shortcuts import get_object_or_404, render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.http import HttpResponse, HttpResponseRedirect




def register(request):
        if request.method == 'POST':  
            form = UserCreationForm(request.POST)  
            if form.is_valid():  
                form.save() 
                response=redirect('/upload')
                return response
        else:
            form = UserCreationForm() 
        return render(request, 'store/register.html', {'form':form}  )
def logout_user(request):
    logout(request)
    messages.success(request,("AI fost deconectat cu succes "))

def register_user(request):
    return render(request,'')


def cart(request):
    context={}
    return render(request, 'store/cart.html', context)

def search(request):
    if request.method=="POST":
        searched =request.POST['searched']
        products_s=Product.objects.filter(part_number__contains=searched)
        return render (request, "store/search",{'searched':products_s})
    else:
        return render(request, 'store/search.html')
       



# Create d views here.
def checkout(request):
    context={}
    return render(request, 'store/checkout.html' ,context)
# Create d views here.

def all_products(request):
    products =Product.products.all()
    return render(request, 'store/home.html',{'products':products})


def product_detail(request,slug):
    product=get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/products/detail.html',{'product':product})

def category_list(request,category_slug=None):
    category=get_object_or_404(Category, slug=category_slug)
    products=Product.objects.filter(category_p=category)
    return render(request, 'store/products/category.html',{'category':category,'products':products})

def upload(request):
    products =Product.products.all()
    if request.method == 'POST':
        uploaded_file =request.FILES['image']
        fs=FileSystemStorage()
        file_name=fs.save(uploaded_file.name, uploaded_file)
        file_url=fs.path(file_name)
        
        with open('labels.txt', 'r') as f:
            class_names= f.read().split('\n')
        data = np.ndarray(shape=(1, 224, 224, 3), dtype=np.float32)
        image = Image.open(file_url)
        size = (224, 224)
        image = ImageOps.fit(image, size, Image.ANTIALIAS)

#turn the image into a numpy array
        image_array = np.asarray(image)
# Normalize the image
        normalized_image_array = (image_array.astype(np.float32) / 127.0) - 1
# Load the image into the array
        data[0] = normalized_image_array

# run the inference
      
        prediction=settings.IMAGE_MODEL.predict(data)
        index = np.argmax(prediction)
        class_name = class_names[index]
        confidence_score =prediction[0][index]
        os.remove(file_url)
        
    else:
        return render(request, 'store/upload.html')
    return render(request, 'store/upload.html',{"categoria":class_name,"sim":confidence_score,"products":products})     
