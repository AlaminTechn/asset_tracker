from django.utils import timezone

from django.db import models


class Company(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'company'
        verbose_name = 'Company'
        verbose_name_plural = 'Company'

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

    class Meta:
        db_table = 'employee'
        verbose_name = 'Employee'
        verbose_name_plural = 'Employee'

    def __str__(self):
        return self.name


class Device(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'device'
        verbose_name = 'Device'
        verbose_name_plural = 'Device'

    def __str__(self):
        return self.name


class DeviceLog(models.Model):
    device_name = models.ForeignKey(Device, on_delete=models.CASCADE)
    employee_name = models.ForeignKey(Employee, on_delete=models.CASCADE)
    check_out_at = models.DateTimeField(default=timezone.now)
    check_in_at = models.DateTimeField(null=True, blank=True)
    condition_when_checked_out = models.CharField(max_length=100)
    condition_when_checked_at = models.CharField(max_length=100, null=True, blank=True)

    class Meta:
        db_table = 'device_log'
        verbose_name = 'Device Log'
        verbose_name_plural = 'Device Log'

    def __str__(self):
        return f"{self.employee_name} taking device : {self.device_name}"
