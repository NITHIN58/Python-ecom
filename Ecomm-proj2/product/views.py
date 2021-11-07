from django.shortcuts import render
from django.http import HttpResponse,request
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render ,redirect
from .models import Product
from ekart.models import User
from vendor.models import Vendor
from .models import Category
from pathlib import Path
#pandas
import pandas as pd
import os
BASE_DIR = Path(__file__).resolve().parent.parent
# Create your views here.

#csv
# def generate(request):
#     df=pd.DataFrame(Product.objects.all().values())
#     datas=Product.objects.all()

#     if request.method=='POST':
def generate(request):
   
    df=pd.DataFrame(Product.objects.all().values())
    datas=Product.objects.all()
    v=Vendor.objects.all()
    if request.method=="POST":
        from1=request.POST.get('pricefrom')
        to=request.POST.get('priceto')
        
        df=pd.DataFrame(Product.objects.filter(price_gte=from1,price_lte=to))
        datas=Product.objects.filter(price_gte=from1,price_lte=to)
        return render(request,"viewProduct.html",{'product':datas})
    path=os.path.join(BASE_DIR,'media/csvfile/products.csv')
    df.to_csv(path)
    return render(request,"viewProduct.html",{'product':datas})

def report(request):
    k=Product.objects.all()
    v=Vendor.objects.all()
    df=pd.DataFrame(Product.objects.all().values())
    path=os.path.join(BASE_DIR,'media/csvfile/products.csv')
    df.to_csv(path)

    if request.method=='POST':
        searchcategory=request.POST.get("searchcategory")
        if(searchcategory !=""):
            f=Product.objects.filter(Product_Category__Category_Name=searchcategory)
        searchvendor=request.POST.get("searchvendor")
        # if(searchvendor !=""):
        #     f=Product.objects.filter(vendor__username=searchvendor)
        searchname=request.POST.get("searchname")
        if(searchname !=""):
            f=Product.objects.filter(Product_Name=searchname)
        return render(request,"viewProduct.html",{'product':f,'ven':v})
    return render(request,"viewProduct.html",{'product':k,'ven':v})

def filterprice(request):
        if request.method=="POST":
            pfrom=request.POST.get("pricefrom")
            pto=request.POST.get("priceto")
            k=Product.objects.filter(Product_Price__range=(pfrom,pto))
            df=pd.DataFrame(Product.objects.filter(Product_Price__range=(pfrom,pto)))
            path=os.path.join(BASE_DIR,'media/csvfile/products.csv')
        df.to_csv(path)
        return render(request,"viewProduct.html",{'product':k})


def addAdmin(request):
    c=Category.objects.all()
    if request.method=="POST":
        Product_Name=request.POST.get("Product_Name")
        Product_Discription=request.POST.get("Product_Discription")
        Product_Price=request.POST.get("Product_Price")
        Product_Stock=request.POST.get("Product_Stock")
        Product_Stock_Status=request.POST.get("Product_Stock_Status")
        Product_cat=request.POST.get("Product_Category")
        Product_Category=Category.objects.get(Category_Name=Product_cat)
        Product_Image=request.FILES["Product_Image"]
        f=FileSystemStorage()
        fp = f.save(Product_Image.name,Product_Image)
        Product.objects.create(Product_Name=Product_Name,Product_Discription=Product_Discription,Product_Price=Product_Price,Product_Stock=Product_Stock,Product_Stock_Status=Product_Stock_Status,Product_Category=Product_Category,Product_Image=fp)
    return render(request,"addproduct.html",{'cat':c})



def signout (request) :
    return redirect("home")
   

def dashboard(request):
    return render(request, "dashboard.html")


# Product Report


#view and filter by category
def viewProducts(request):
    k=Product.objects.all()
    v=Vendor.objects.all()
    if request.method=="POST":
        na=request.POST.get("filt")
        f= Product.objects.filter(Product_Category__Category_Name=na)
        return render(request,"viewProduct.html",{'product':f})
    return render(request,"viewProduct.html" ,{"product":k,"pro":v})

#filterby name
def filterName(request):
    A=Product.objects.all()
    if request.method=="POST":
        na=request.POST.get("filterName")
        nm=Product.objects.filter(Product_Name=na)
        return render(request,"viewProduct.html",{"product":nm})
    return render(request, "viewProduct.html",{"product":A})

def filterVendor(request):
    v=Vendor.objects.all()
    if request.method=="POST":
        na=request.POST.get("vendorName")
        nm=Vendor.objects.filter(vendor_name=na)
        return render(request,"viewProduct.html",{"product":nm,"pro":nm})
    return render(request, "viewProduct.html",{"product":A,"pro":v})


def updateProduct(request,userid):
    c=Category.objects.all()
    k=Product.objects.filter(id=userid).values()
    if request.method == "POST":
        Product_Name=request.POST.get("Product_Name")
        Product_Discription=request.POST.get("Product_Discription")
        Product_Price=request.POST.get("Product_Price")
        Product_Stock=request.POST.get("Product_Stock")
        Product_Stock_Status=request.POST.get("Product_Stock_Status")
        Product_cat=request.POST.get("Product_Category")
        Product_Category=Category.objects.get(Category_Name=Product_cat)
        Product_Image=request.FILES["Product_Image"]
        f=FileSystemStorage()
        fp = f.save(Product_Image.name,Product_Image)
        k=Product.objects.filter(id=userid).values()
        k.update(Product_Name=Product_Name,Product_Discription=Product_Discription,Product_Price=Product_Price,Product_Stock=Product_Stock,Product_Stock_Status=Product_Stock_Status,Product_Category=Product_Category,Product_Image=fp) 
        return redirect("view")
    return render(request, "productUpdate.html",{"product":k[0],"id":userid,"cat":c})

def deletePro(request,userid):
    c=Product.objects.filter(id=userid)
    c.delete()
    return redirect("view")

#category

def addCat(request):
    if request.method=="POST":
        print(request.POST)
        Category_Name=request.POST.get("Category_Name")
        Category_Discription=request.POST.get("Category_Discription")
        Category.objects.create(Category_Name="Category_Name",Category_Discription="Category_Discription")
    return render(request,"addCategory.html")

#logout  
def signout(request):
    logout(request)
    return redirect('home')

