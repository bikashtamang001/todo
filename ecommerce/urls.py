from rest_framework import routers
from django.urls import path, include
from . import views

router = routers.DefaultRouter(trailing_slash = False)
router.register('product/',views.ProductViewSet)
router.register('category/',views.CategoryViewSet)

urlpatterns= []
urlpatterns += router.urls