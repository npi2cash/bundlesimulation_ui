from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportModelAdmin
from import_export import resources
from .models import Product,SalesData
# Register your models here.
@admin.register(Product)
class userdat(ImportExportModelAdmin):  
    pass

@admin.register(SalesData)
class userdat(ImportExportModelAdmin): 
    model=SalesData
    fields=['Sales_Doc_Number'] 
    import_id_field=('Sales_Doc_Number')




   
        