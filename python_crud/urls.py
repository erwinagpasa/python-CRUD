from django.contrib import admin
from django.urls import path
from .import views  # importing views.py


urlpatterns = [
    path('admin/', admin.site.urls),
    path('about/', views.about),
    path('', views.homepage),
]
