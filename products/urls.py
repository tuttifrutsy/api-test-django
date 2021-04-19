from django.urls import path

from .views import ProductViewSet, userAPIView

urlpatterns = [
    path('products', ProductViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('products/<str:pk>', ProductViewSet.as_view({
        'get': 'retrive',
        'put': 'update',
        'delete': 'destroy'
    })),
    path('user', userAPIView.as_view())
]