
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from matplotlib.pyplot import plot_date

from . import views
app_name='store'

urlpatterns = [
	path('cart/', views.cart, name="cart"),
	path('search/', views.search, name="search"),
	path('upload/',views.upload,name="upload"),
	path('register/',views.register,name="register"),
	path('', views.all_products,name='all_products'),
	path('item/<slug:slug>/',views.product_detail,name='product_detail'),
	path('categories/<slug:category_slug>/',views.category_list,name='category_list'),
]
