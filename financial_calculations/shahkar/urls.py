from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import IncomeCalculationsViewSet

router = DefaultRouter()
router.register(r'income-calculations', IncomeCalculationsViewSet, basename='income-calculations')

urlpatterns = router.urls
