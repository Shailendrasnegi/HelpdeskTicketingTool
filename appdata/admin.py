from django.contrib import admin
from .models import FirstData

@admin.register(FirstData)
class Customer(admin.ModelAdmin):
    list_display = ['id', 'Customer_Name', 'Customer_Detail', 'Mail_ID', 'Service_ID', 'Service_Type', 'Problem_Description']


