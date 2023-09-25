from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


from emphub.models import Employee
from api.serializers import EmployeeSearializer

# Create your views here.
class EmployeeView(ModelViewSet):
    serializer_class=EmployeeSearializer
    queryset=Employee.objects.all()
    model=Employee
    http_method_names=['get']










    
