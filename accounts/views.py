from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend # type: ignore
from .models import Accounts
from .serializers import AccountsSerializer
 
class AccountsViewSet(viewsets.ModelViewSet):
    queryset = Accounts.objects.all()
    serializer_class = AccountsSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['org_name', 'email', 'phone', 'address', 'license_no']
    ordering_fields = ['org_name', 'email', 'phone', 'license_no']