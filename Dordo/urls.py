"""Dordo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from med.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/',LoginView),
    path('signup/',SignupView),
    path('signin/',SigninView),
    path('index/',IndexView ),
    path('out/',LogoutView),
    path('profile/',ProfileView),
    path('contact/',ContactView),
    path('about/',AboutView),
    path('productinfo/<int:id>/',ProductInfoView),
    path('cart/',CartView),
    path('addtocart/<int:id>/', Add_to_cartView, name='addtocart'),
    path('pluscart/<int:id>/', pluse_quantity),
    path('minuscart/<int:id>/', minus_quantity),
    path('Delete/<int:id>/',DeleteView),
    path('clearcart/', clearcart),
    path('Listdelete/<int:id>/',ListDeleteView),
    path('address/',CustomerAddressView),
    path('Addressdelete/<int:id>/',AddressDeleteView),
    path('Addressupdate/<int:id>/',UpdateaddressView),
    path('order/', OrderView),
    path('checkout/', CheckoutView),
    path('allproducts/',AllproductView),
    
  
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
