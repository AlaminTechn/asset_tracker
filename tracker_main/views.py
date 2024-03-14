from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK, HTTP_400_BAD_REQUEST
from rest_framework.views import APIView

from .models import Company, Device, Employee, DeviceLog
from .serializers import CompanySerializer, EmployeeSerializer, DeviceSerializer, DeviceLogSerializer


class CompanyListAPI(APIView):
    permission_classes = []

    def get(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Success',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Company Not Found',
                'data':    []
        }

        queryset = Company.objects.all()
        companies_serializer = CompanySerializer(queryset, many=True).data

        if companies_serializer:
            result['data'] = companies_serializer
            return Response(result)
        return Response(result_error)


class EmployeeListAPI(APIView):
    permission_classes = []

    def get(self, request):
        result = {
                'status':  HTTP_200_OK,
                'message': 'Success',
                'data':    []
        }

        result_error = {
                'status':  HTTP_400_BAD_REQUEST,
                'message': 'Employee Not Found',
                'data':    []
        }

        queryset = Employee.objects.all()
        employee_serializer = EmployeeSerializer(queryset, many=True).data

        if employee_serializer:
            result['data'] = employee_serializer
            return Response(result)
        return Response(result_error)
