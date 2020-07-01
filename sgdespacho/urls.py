from django.urls import path
from rest_framework import routers
from .viewset import PaqueteViewSet,BodegaViewSet


from django.urls import path,include


router = routers.DefaultRouter()
router.register('paquete',PaqueteViewSet)
router.register('bodega',BodegaViewSet)
urlpatterns = router.urls



