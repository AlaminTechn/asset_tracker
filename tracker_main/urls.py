from django.contrib import admin
from django.urls import path, include
from .views import CompanyListAPI, EmployeeListAPI

urlpatterns = [
        path('company-list/', CompanyListAPI.as_view()),
        path('employee-list/', EmployeeListAPI.as_view()),
]
