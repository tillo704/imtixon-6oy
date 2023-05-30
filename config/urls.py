from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from api.views import CustomListCreatAPIView



urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('api.urls')),
    path('api-auth/',include('rest_framework.urls'))
]
