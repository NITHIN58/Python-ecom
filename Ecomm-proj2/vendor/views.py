from django.shortcuts import render
from django.shortcuts import render ,redirect
from django.http import HttpResponse,request
# Create your views here.
from .models import Vendor


def addVender(request):
    if request.method=="POST":
        branch=request.POST.get("branch")
        vendor_name=request.POST.get("vendor_name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        address=request.POST.get("address")
        Vendor.objects.create(branch=branch,vendor_name=vendor_name,phone_number=phone_number,email=email,username=username,password=password,address=address)
    return render(request,"Vendor.html")

def listVendor(request):
    k=Vendor.objects.all()
    if request.method=="POST":
        branch=request.POST.get("branch")
        vendor_name=request.POST.get("vendor_name")
        phone_number=request.POST.get("phone_number")
        email=request.POST.get("email")
        username=request.POST.get("username")
        password=request.POST.get("password")
        address=request.POST.get("address")
        Vendor.objects.create(branch=branch,vendor_name=vendor_name,phone_number=phone_number,email=email,username=username,password=password,address=address)
    return render(request, "vendorList.html",{"vendor":k})