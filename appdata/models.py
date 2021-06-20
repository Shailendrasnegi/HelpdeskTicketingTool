from django.db import models

# Create your models here.
class FirstData(models.Model):
    Customer_Name = models.CharField(max_length= 10)
    Customer_Detail = models.CharField(max_length=100)
    Mail_ID = models.EmailField()
    Service_ID = models.IntegerField()
    Service_Type = models.CharField(max_length=20)
    Problem_Description = models.TextField(max_length=200)