from rest_framework import viewsets
from .models import Paquete,Bodega
from .serializers import PaqueteSerializer,BodegaSerializer

class PaqueteViewSet(viewsets.ModelViewSet):
    queryset = Paquete.objects.all()
    serializer_class=PaqueteSerializer

class BodegaViewSet(viewsets.ModelViewSet):
    queryset=Bodega.objects.all()
    serializer_class=BodegaSerializer
