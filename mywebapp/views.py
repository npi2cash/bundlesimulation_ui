from django.db.models.query import QuerySet
from django.db.models.sql.query import Query
from django.shortcuts import render,redirect
from django.http import HttpResponse, response
from .forms import modelform
from .models import Product
from django.db.models import Q
from django.db.models import query_utils
# Create your views here.
def home(request):
    form=modelform(request.GET)
    kwargs = {}
    if request.GET:
        if request.GET['Cluster']!="Select a Value":
            cluster=request.GET['Cluster']
            kwargs['Cluster']=cluster
        if request.GET['Business']!="Select a Value":
            business=request.GET['Business']
            kwargs['Business']=business
        if request.GET['Category']!="Select a Value":
            category=request.GET['Category']
            kwargs['Category']=category
        if request.GET['Product_Code']!="Select a Value":
            product_code=request.GET['Product_Code']
            kwargs['Product_id']=product_code
        print(kwargs)
        obj=Product.objects.filter(**kwargs)
    else:
        obj=Product.objects.all()
    context={'filterform':form,'products':obj}
    return render(request,'home.html',context)

def Reset(request):
    form=modelform()
    obj=Product.objects.all()
    context={'filterform':form,'products':obj}
    return render(request,'home.html',context)