"""superlists URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from lists.views import home_page, view_list, new_list, add_item
from django.urls import path, re_path

urlpatterns = [
    path('', home_page, name="home"),
    re_path(r'^lists/new/$', new_list, name="new_list"),
    re_path(r'^lists/(\d+)/$', view_list, name="view_list"),
    re_path(r'^lists/(\d+)/add_item$', add_item, name="view_list"),    
    # path('admin/', admin.site.urls),
]
