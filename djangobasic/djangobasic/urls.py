"""djangobasic URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from django.contrib import admin
from django.urls import path, re_path, include

#http요청이 들어올 때마다 등록된 urlpatterns상의 매핑 리스트를 처음부터 순차적으로 훑으며 매핑 시도

urlpatterns = [
    path('admin/', admin.site.urls), #어떠한 url이 들어오면 어떠한 함수를 호출할건지
    path('shop/', include('shop.urls')),
]
