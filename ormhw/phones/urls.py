from django.urls import path
from .views import CatalogView, PhoneDetailView

urlpatterns = [
    path('', CatalogView.as_view(), name='catalog'),  # Основной маршрут для каталога
    path('<slug:slug>/', PhoneDetailView.as_view(), name='phone_detail'),  # Подробности о телефоне
]