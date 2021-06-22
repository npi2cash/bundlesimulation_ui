from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Product(models.Model):
    id=models.AutoField(primary_key=True)
    Catalog_release=models.CharField(max_length=200,default='nill')
    Cluster=models.CharField(max_length=200)
    Business=models.CharField(max_length=200)
    Category=models.CharField(max_length=200)
    Equipment_Type=models.CharField(max_length=200)
    Item_Type=models.CharField(max_length=200)
    Ownership=models.CharField(max_length=200)
    Product_id=models.CharField(max_length=200,unique=True)
    Name=models.CharField(max_length=200)
    NumberofmonthstheitemhasbeeninApttus=models.IntegerField(default=0)
    Itemequalorlessthan12monthsold=models.CharField(max_length=200)
    OITContribution_18m=models.CharField(max_length=200,default='nill')
    OITValue_18mo=models.CharField(max_length=200,default='nill')
    OITContribution_36m=models.CharField(max_length=200,default='nill')
    OITValue_36mo=models.CharField(max_length=200,default='nill')
    Orderedinthelast_18m=models.CharField(max_length=200,default='nill')
    Orderedinthelast_36m=models.CharField(max_length=200,default='nill')

    def __str__(self):
        return self.Cluster



class SalesData(models.Model):
    id=models.IntegerField(default=0)
    Sales_Doc_Number=models.IntegerField(default=0)
    Year_Month=models.CharField(max_length=200,default='nill')
    Market=models.CharField(max_length=200,default='nill')
    Business=models.CharField(max_length=200,default='nill')
    Category=models.CharField(max_length=200,default='nill')
    Product_Code=models.ForeignKey(Product,on_delete=models.CASCADE,to_field='Product_id')
    Product_Name=models.IntegerField(primary_key=True)
    Options=models.CharField(max_length=200,default='nill')
    WRP=models.DecimalField(decimal_places=5,max_digits=10)
    Option_Name=models.CharField(max_length=200,default='nill')
    OIT_value=models.DecimalField(decimal_places=5,max_digits=10)
    Quantity=models.IntegerField(default=0)
    Bundle_Marker_Flag=models.CharField(max_length=3,default='N')
    Sales_Order_with_Bundle=models.CharField(max_length=3,default='N')
    
    def __str__(self):
        return self.Sales_Doc_Number


    