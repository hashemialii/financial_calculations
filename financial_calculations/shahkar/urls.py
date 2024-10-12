from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeViewSet


router = DefaultRouter()
router.register(r'income', IncomeViewSet, basename='income')

# استفاده از router در urlpatterns
urlpatterns = [
    path('', include(router.urls)),
]
