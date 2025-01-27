from django.urls import path
from .views import ProdutoList

urlpatterns = [
    path('produtos/', ProdutoList.as_view(), name='produto-list'),
]