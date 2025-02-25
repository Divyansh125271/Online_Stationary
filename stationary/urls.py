"""
URL configuration for stationary project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from myapp import views
from django.urls.conf import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('home',views.home),
    path('log',views.log),
    path('out',views.out),
    path('SignUp',views.SignUp),
    path('admin',views.admin),
    path('admindashboard',views.admindashboard),
    path('addproduct',views.addproduct),
    path('viewproduct',views.viewproduct),
    path('manageproduct',views.manageproduct),
    path('delete/<int:data>',views.desk),
    path('edit/<int:data>',views.editt),
    path('edit/update/<int:data>',views.upd),
    path('bag',views.bag),
    path('cart/<int:id>',views.cart),
    path('dele/<int:data>',views.dele),
    path('ordernow',views.order),
    path('viewcustomer',views.vcustomer),
    path('vieworder',views.vorder),
    path('contactus',views.contact),
    path('mail',views.mail),
    path('aboutus',views.about),
    path('status/<int:id>',views.status),
    path('trackorder',views.track)
    
]
if settings.DEBUG:urlpatterns +=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
