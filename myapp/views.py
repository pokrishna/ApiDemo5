from rest_framework import filters
from django.shortcuts import render
from myapp.models import Employee
from myapp.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny,IsAdminUser,IsAuthenticatedOrReadOnly,DjangoModelPermissions
from myapp.permissions import IsReadOnly,IsGETOrPatch,NameCheckPermission
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.pagination import PageNumberPagination

class EmployeeCBV(ModelViewSet):
    serializer_class=EmployeeSerializer
    queryset=Employee.objects.all()
    # authentication_classes=[JSONWebTokenAuthentication,]
    # permission_classes=[IsAuthenticated,]
    pagination_class=PageNumberPagination
    filter_backends = [filters.SearchFilter,filters.OrderingFilter]
    search_fields = ['ename','eno']
    ordering_fields = ['eno','esal']
