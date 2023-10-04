"""
URL configuration for ERP_MK1 project.

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
from INOUT import views as ino

urlpatterns = [
    path('admin/', admin.site.urls),
    path('' , ino.login ),
    path('index/' , ino.landingpage , name = 'landingpage') ,
    path('login_check/' , ino.check_login) ,
    path('login/' , ino.login_page),
    path('stock_update/' , ino.stockupdate),
    path('ref/' , ino.input_data),
    path('stock_update_save/' , ino.stock_update_save),
    path ('stock_update_table/' , ino.stock_update_table),
    path ('/stock_update/stock_update_table/' , ino.stock_update_table),
    path('update_stock_form/' , ino.update_stock),
    path('save_stock_data/' , ino.save_stock_data),
    path('update_outwards_form/' , ino.update_outward),
    path('view_stock_detail/' , ino.view_stock_detail),
path('view_outwards_detail/' , ino.view_outwards_detail),
    # path('save_stock_data/' , ino.save_stock_data),view_stock_detail view_outwards_detail

]
