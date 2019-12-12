from django.urls import path
from . import views

app_name = 'api'
urlpatterns = [
    path('', views.ProductListView.as_view(), name='product_list'),
    path('create/', views.ProductCreateView.as_view(), name='product_add'),
    path('<int:pk>/', views.ProductDetailView.as_view(), name='product_detail')
]
