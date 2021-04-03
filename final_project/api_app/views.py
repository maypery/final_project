from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import Employee
from .serializers import EmployeeSerializer
# Create your views here.


class EmployeeView(viewsets.ModelViewSet):
    queryset = Employee.objects.all().defer('image')
    serializer_class = EmployeeSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


def EmployeeViewHTML(request):
    employees = Employee.objects.all().order_by('employee_id')
    return render(request, "employees.html", {"employees": employees})

