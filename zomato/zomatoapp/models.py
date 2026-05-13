from django.db import models
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

