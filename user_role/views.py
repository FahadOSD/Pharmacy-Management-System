from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .models import UserRole
from .serializers import UserRoleSerializer

class UserRoleViewSet(viewsets.ModelViewSet):
    queryset = UserRole.objects.all()
    serializer_class = UserRoleSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter]
    
    filterset_fields = ['role']
    search_fields = ['acc_id__org_name']