from django.urls import path
from . import views

urlpatterns = [
    path('', views.category_list, name='category_list'),
    path('add/', views.category_add, name='category_add'),
    path('edit/<int:pk>/', views.category_edit, name='category_edit'),
]
from django.urls import path, include

urlpatterns = [
    # existing paths...
    path('categories/', include('apps.categories.urls')),
]