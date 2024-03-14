from rest_framework import serializers
from .models import Company, Employee, Device, DeviceLog


class CompanySerializer(serializers.Serializer):
    class Meta:
        model = Company
        fields = '__all__'


class EmployeeSerializer(serializers.Serializer):
    class Meta:
        model = Employee
        fields = '__all__'
        readonly_fields = ['name', 'company', ]


class DeviceSerializer(serializers.Serializer):
    class Meta:
        model = Device
        fields = '__all__'


class DeviceLogSerializer(serializers.Serializer):
    class Meta:
        model = DeviceLog
        fields = ['device_name', 'employee_name', 'check_out_at', 'check_in_at', 'condition_when_checked_out', 'condition_when_checked_at']
