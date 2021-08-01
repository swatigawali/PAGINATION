from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import generics
from .pagination import MyPagination,MyPagination2,MyPagination3

# Create your views here.
class EmployeeAPIView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=MyPagination

'''
class EmployeeAPIView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=MyPagination2


class EmployeeAPIView(generics.ListAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer
    pagination_class=MyPagination3
'''