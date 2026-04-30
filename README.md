# Ex01 Django ORM Web Application
## Date: 30-04-26

## AIM
To develop a Django application to manage an online food delivery platform like Zomato/Swiggy using Object Relational Mapping (ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
MODELS:
```from django.db import models
from django.contrib import admin
from django.db import models

class OrderTransaction(models.Model):
    OrderID = models.IntegerField(primary_key=True)
    UserID = models.IntegerField()
    OrderDate = models.DateTimeField(auto_now_add=True)
    ItemName = models.CharField(max_length=200)
    OrderQty = models.IntegerField()
    UnitPrice = models.DecimalField(max_digits=10, decimal_places=2)
    TotalAmount = models.DecimalField(max_digits=10, decimal_places=2)
    DeliveryAddress = models.CharField(max_length=300)
class OrderTransactionAdmin(admin.ModelAdmin):
    list_display=('OrderID','UserID','OrderDate','ItemName','OrderQty','UnitPrice','TotalAmount','DeliveryAddress')    
```
ADMIN:
```from django.contrib import admin

from .models import OrderTransaction,OrderTransactionAdmin
admin.site.register(OrderTransaction,OrderTransactionAdmin)
```




## OUTPUT

<img width="608" height="440" alt="image" src="https://github.com/user-attachments/assets/ccbf0bc0-0a66-44ad-9b0a-ede15e8239b4" />

<img width="1915" height="901" alt="image" src="https://github.com/user-attachments/assets/c4a6c6d8-a6d5-4b30-8e1e-73e89d63f730" />

## RESULT
Thus the program for creating a database using ORM hass been executed successfully
