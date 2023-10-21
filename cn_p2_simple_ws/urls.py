"""
URL configuration for cn_p2_simple_ws project.

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
from django.urls import path
from practica2c_grupo5_simple_ws.views import (
    DirectoryListCreateAPIView,
    DirectoryRetrieveUpdateDestroyAPIView,
    StatusApiView,
)

urlpatterns = [
    path('status/', StatusApiView.as_view()),
    path('directories/', DirectoryListCreateAPIView.as_view()),
    path('directories/<int:pk>',
         DirectoryRetrieveUpdateDestroyAPIView.as_view()),
]
