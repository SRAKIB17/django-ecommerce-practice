
from django.contrib import admin
from django.urls import path, include
from apps.products import views


urlpatterns = [
    path("/", include('apps.products.urls'), name="home"),
    path("", include('apps.products.urls'), name="home"),
    path('admin/', admin.site.urls),
]
