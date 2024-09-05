from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from .models import Drug
from .serializers import DrugSerializer

class DrugViewSet(viewsets.ModelViewSet):
    queryset = Drug.objects.all()
    serializer_class = DrugSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'type', 'price', 'acc_id__org_name']  
    ordering_fields = ['name', 'type', 'price', 'acc_id__org_name']  

