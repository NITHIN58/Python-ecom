
from django.shortcuts import render ,redirect
from django.http import HttpResponse,request
from .models import *
from .models import User
from vendor.models import Vendor
from product.models import Product,Category
from django.contrib.auth import authenticate,login,logout
from django.core.files.storage import FileSystemStorage
from ekart.models import User


# Create your views here.
def registration(request):
    if request.method=='POST':
        fm=request.POST.get("firstname")
        ln=request.POST.get("lastname")
        em=request.POST.get("email")
        mb=request.POST.get("mobile")
        ad=request.POST.get("address")
        cy=request.POST.get("city")
        rl=request.POST.get("roles")
        pc=request.POST.get("postcode")
        pw=request.POST.get("password")
        im=request.FILES['profilepic']
        f=FileSystemStorage()
        fp=f.save(im.name,im)
        User.objects.create(first_name=fm,last_name=ln,email=em,phone=mb,address=ad,city=cy,postcode=pc,password=pw,profilepic=fp,role=rl)
        return HttpResponse("you can now login")
    return render(request, 'login.html')






def temp(request):
    p=Product.objects.all()
    c=Category.objects.all()
    print(p)
    return render(request,"index.html",{'product':p,'category':c})
#category 


def dashboardfront(request):
    pc=Product.objects.all().count()
    uc=User.objects.all().count()
    oc=order.objects.all().count()
    vc=Vendor.objects.all().count()
    return render(request,"dashtotal.html",{'productcount':pc,'usercount':uc,'ordercount':oc,'vendorcount':vc})




# def user_login(request):
#     if request.method=="POST":
#         em=request.POST.get("email")
#         pw=request.POST.get("password")
#         if User.objects.filter(Email=em,Password=pw).exists():
#             #new
#             # datas=User_Model.objects.filter(Email=em,Password=pw).values().first
#             # print(datas)
#             # request.session['em']=datas['Email']
#             return redirect('home')
#         else:
#             return HttpResponse("<h1>invalid user! please enter correct details</h1>")
#     return render(request, "login.html")



def user_login(request):
    if request.method=="POST":
        em=request.POST.get("email")
        pw=request.POST.get("password")
        user=authenticate(request,email=em,password=pw)
        if user:
            login(request,user)
            print(request.user)
            return render(request,"index.html")
        else:
            return HttpResponse("<h1>invalid  login details</h1>")
            return render(request, "login.html")
    return render(request, "login.html")


#use logout
def signout(request):
    logout(request)
    return redirect('reg')


##change password

# def updatepass(request):
#      u=user.objects.get(email="nithin@gmail.com")
#      u.set_password("nithin@123")
#      u.save()
#      return HttpResponse("password updated")


def updatepass(request):
     u=User.objects.get()
     u.set_password("nithin@123")
     u.save()
     return HttpResponse("password updated")


def myaccount(request):
        return render(request,"my-account.html")

#add oder  and order list

def addorder(request):
    c=User.objects.all()
    v=vendor.objects.all()
    if request.method=="POST":
        order_date=request.POST.get("order_date")
        customer_id=request.POST.get("customer_id")
        vendor_id=request.POST.get("vendor_id")
        order_total=request.POST.get("order_total")
        payment_method=request.POST.get("payment_method")
        delivery_date=request.POST.get("delivery_date")
        status=request.POST.get("status")
        Is_deliverd=request.POST.get("Is_deliverd")
        order.objects.create(order_date=order_date,customer_id=customer_id,vendor_id=vendor_id,order_total=order_total,payment_method=payment_method,delivery_date=delivery_date,status=status,Is_deliverd=Is_deliverd)
        return HttpResponse("order added")
    return render(request, "AddOrder.html")

    #customer


def Addcustomer(request):
    c=User.objects.all()
    if request.method=='POST':
        fm=request.POST.get("firstname")
        ln=request.POST.get("lastname")
        em=request.POST.get("email")
        mb=request.POST.get("mobile")
        ad=request.POST.get("address")
        cy=request.POST.get("city")
        rl=request.POST.get("role")
        pc=request.POST.get("postcode")
        pw=request.POST.get("password")
        pw2=request.POST.get("password2")
        im=request.FILES['profilepic']
        f=FileSystemStorage()
        fp=f.save(im.name,im)
        User.objects.create(first_name=fm,last_name=ln,email=em,phone=mb,address=ad,city=cy,postcode=pc,password=pw,profilepic=fp,password2=pw2)
        return HttpResponse("you can now login")
    return render(request, 'Customer.html',{'customer':c})

#customer
def viewcustomer(request):
    k=User.objects.all()
      
    return render(request, "customerList.html",{'customer':k})


#order
def viewOrder(request):
    allorder=order.objects.all()
    alluser=User.objects.all()
    allvendor=Vendor.objects.all()
    d=Product.objects.all()
    if request.method == "POST":
        Product_Name=request.POST.get("Product_Name")
        v=Product.objects.get(Product_Name="shoe")
        #v=Product.objects.get(Product_Name=Product_Name)
        quantity=int(request.POST.get("quantity")) 
        m=Product.objects.filter(Product_Name=Product_Name).values()
        v_price=v.Product_Price 
        o_subtotal=int(quantity*v_price)
        p_quantity=int(v.Product_Stock)
        cprice=p_quantity-quantity  
        order_date=request.POST.get("order_date") 
        customer_id=request.POST.get("Product_Category")
        print(customer_id)  
        l=User.objects.get(email=customer_id)
        vendor_id=request.POST.get("Vender")              
        vendor_id=request.POST.get("Vender")
        k=Vendor.objects.get(username=vendor_id)           
        payment_method=request.POST.get("payment_method")       
        payment_status=request.POST.get("payment_status")       
        delivery_date=request.POST.get("delivery_date")       
        status=request.POST.get("status")   
        Is_delivered=request.POST.get("Is_delivered")
        if(p_quantity==0):
            m.update(Product_Stock_Status="false")
            return HttpResponse("product out of stock")
        else:
            if((p_quantity)>=quantity):
                x=order.objects.create(order_date=order_date,customer_id=l,vendor_id=k,order_total=o_subtotal,payment_method=payment_method,delivery_date=delivery_date,status=status,Is_deliverd=Is_delivered)
                orderdetails.objects.create(product_id=v,product_qty=quantity,product_price=v_price,subtotal=o_subtotal,order=x)
                m.update(Product_Stock=cprice) 
                return redirect("viewOrder")
            else:
                return HttpResponse("order could not be completed :product required greater than stock")
    return render(request,"AddOrder.html",{"product":allorder,"user":alluser,"vendors":allvendor,"pr":d})
        

        
    #     if(Is_delivered==None):
    #         Is_delivered=False
    #         x=order.objects.create(order_date=order_date,customer_id=l,vendor_id=k,order_total=order_total,payment_method=payment_method,payment_status=payment_status,delivery_date=delivery_date,status=status,Is_delivered=Is_delivered)
    #         orderdetails.objects.create()
    #     return redirect("viewOrder")
    # return render(request,"AddOrder.html",{"product":c,"user":m,"vendors":n})

#filters

def filterbyid(request):
        k=order.objects.all()
        if request.method=="POST":
            na=request.POST.get("filterbyid")
            sa=order.objects.filter(customer_id__email=na)
            print(sa)
            return render(request,"AddOrder.html",{'product':sa})
        return render(request,"AddOrder.html",{'product':k})

def filtorderbydate(request):
    k=order.objects.all()
    if request.method=="POST":
        ca=request.POST.get("filterordate")
        sa=order.objects.filter(delivery_date=ca)
        return render(request,'AddOrder.html',{'product':sa})
    return render(request,'AddOrder.html',{'product':k})

def getorder(request):
        k=order.objects.all()
        if request.method=="POST":
            na=request.POST.get("searchorder")
            sa=order.objects.filter(status=na)
            print(sa)
            return render(request,"AddOrder.html",{'product':sa})
        return render(request,"AddOrder.html",{'product':k})
    

def viewmyaccount(request):
        k=order.objects.all()
        if request.method=="POST":
            na=request.POST.get("searchorder")
            sa=order.objects.filter(status=na)
            print(sa)
            return render(request,"my-account.html",{'product':sa})
        return render(request,"my-account.html",{'product':k})
    
#product in frontend

def listProducts(request):
    k=Product.objects.all()
    v=Vendor.objects.all()
    if request.method=="POST":
        na=request.POST.get("filt")
        f= Product.objects.filter(Product_Category__Category_Name=na)
        return render(request,"product-list.html",{'product':f})
    return render(request,"product-list.html" ,{"product":k,"pro":v})
# def cart(request):
#     k=Product.objects.all()
#     v=Vendor.objects.all()
#     if request.method=="POST":
#         na=request.POST.get("filt")
#         f= Product.objects.filter(Product_Category__Category_Name=na)
#         return render(request,"product-list.html",{'product':f})
#     return render(request,"cart.html" ,{"product":k,"pro":v})
def cartadd(request,userid):
    if request.user.is_authenticated :
        k=request.user.id
        mobject=Product.objects.get(id=userid)
        lobject=User.objects.get(id=k)
        addtocart.objects.create(cartuser=lobject,cartproduct=mobject)
        print(k,":added a product to cart")
        return redirect("viewcart")
    else:
        return redirect("register")

        
def viewcart(request):
    s=0
    if request.user.is_authenticated :
        k=request.user.id
        print(k)
        m=User.objects.get(id=k)
        q=addtocart.objects.filter(cartuser__id=k)
        l=addtocart.objects.filter(cartuser=m)
        print(l)
        for i in l:
            print(i)
            n=i.cartproduct_id
            m=i.cartquantity
            print(n,m)
            k=Product.objects.get(id=n)
            o=k.Product_Price
            s=s+o*m
        print(s)
        return render(request,"cart.html",{"product":q,"price":s})
    else:
        return redirect("login")
#delete cart

def deletecart(request,userid):
    #if request.user.is_authenticated :
        n=request.user.id
        m=User.objects.get(id=n)
        o=Product.objects.get(id=userid)
        k=addtocart.objects.filter(cartproduct=o).filter(cartuser=m).first()
        print(k)
        k.delete()
        return redirect("viewcart")
    #return redirect("reg")

#wishlist


def wishlist(request):
    x=[]
    if request.user.is_authenticated :
        k=request.user.id
        m=User.objects.get(id=k)
        l=dbwishlist.objects.filter(wuser=m)
        for i in l:
            n=i.wproduct_id
            print(n)
            k=Product.objects.get(id=n)
            print(k)

            x.append(k)
        print(x)
        return render(request,"wishlist.html",{"product":x})
    else:
        return redirect("register")
def addwishlist(request,userid):
    if request.user.is_authenticated :
        k=request.user.id
        m=Product.objects.get(id=userid)
        l=User.objects.get(id=k)
        dbwishlist.objects.create(wuser=l,wproduct=m)
        print(k,":added a product to wishlist")
        return redirect("wishlist")
    return redirect("reg")


def deletewishlist(request,userid):
    
    if request.user.is_authenticated :
        n=request.user.id
        m=User.objects.get(id=n)
        o=Product.objects.get(id=userid)
        k=dbwishlist.objects.filter(wproduct=o).filter(wuser=m).first()
        print(k)
        k.delete()
        return redirect("wishlist")
    return redirect("reg")
   
def checkout(request):
    x=[]
    v=[]
    s=0
    if request.user.is_authenticated :
        k=request.user.id
        m=User.objects.get(id=k)
        l=addtocart.objects.filter(cartuser=m)
        print(l)
        for i in l:
            print(i)
            n=i.cartproduct_id
            m=i.cartquantity
            print(n,m)
            k=Product.objects.get(id=n)
            o=k.Product_Price
            s=s+o*m
            x.append(k)
            v.append(m)
        print(x,v)
        print(s)
        return render(request,"checkout.html",{"product":x,"quantity":v,"price":s})
    else:
        return redirect("login")

#place order 
# def placeorder(request):
#     uid=request.user.id
#     u=User.objects.get(id=uid)
#     ca=addtocart.objects.filter(cart_user=u)
#     if request.method=="POST":
#         fna=request.POST.get("first_name")
#         lna=request.POST.get("last_name")
#         em=request.POST.get("email")
#         mo=request.POST.get("phone")
#         add=request.POST.get("address")
#         ci=request.POST.get("city")
#         pc=request.POST.get("postcode")
#         pm=request.POST.get("payment_method")
#         st=request.POST.get("state")
#         vname=request.POST.get("vendor_name")
#         dd=datetime.date.today()
#         ddd=dd+datetime.timedelta(days=4)
#         b=User.objects.get(email=u.email)
#         d=Vendor.objects.get(vendor_name=vname)
#         xx=order.objects.create(order_date=dd,order_total=1,payment_method=pm,payment_status=True,delivery_date=ddd,status="Ordered",Is_delivered=False, customer_id=b, vendor_id=d )
#         shipment.objects.create(first_name=fna, last_name=lna, email=em, phone=mo, address=add, city=ci, postcode=pc,state=st, order=xx )
#         for i in ca:
#             sum=0
#             pn=i.cart_product_id
#             pa=Products.objects.get(id=pn)
#             q=i.quantity
#             price=pa.product_price
#             sum=int(price)*int(q)
#             pa.product_stock -= int(q)
#             pa.save()
#             orderdetails.objects.create(product_qty=q, product_price=price,subtotal=sum, order=xx)
#     return render(request,"checkout.html")
def buynow(request,prid): 
    print(prid)
    # if request.user.is_authenticated and  request.method == "POST":
        
    #     k=request.user.id
    #     quantity=int(request.POST.get("quantity")) 
    #     payment=request.POST.get("payment")
    #     customer_id=User.objects.get(id=k) 
    #     product=Product.objects.get(id=prid)
    #     product_fil=Product.objects.filter(id=prid)
    #     vendor_id=product.product_vendor
    #     p_quantity=product.Product_Stock
    #     print(p_quantity)
    #     productprice=product.Product_Price
    #     order_total=quantity*productprice
    #     payment_method=payment
    #     payment_status=False
    #     print(p_quantity,type(p_quantity))
    #     print(quantity,type(quantity))

    #     order_date = datetime.date.today()
    #     if(p_quantity==0):
    #         product_fil.update(Product_Stock_Status=False)
    #         return HttpResponse("product out of stock")
    #     else:
    #         if((p_quantity)>=quantity):
                
    #             x=order.objects.create(order_date=order_date,customer_id=customer_id,order_total=order_total,payment_method=payment_method,payment_status=payment_status,vendor_id=vendor_id)
    #             current_quanty=p_quantity-quantity
    #             product_fil.update(Product_Stock=current_quanty)
    #             orderdetails.objects.create(product_id=product,product_qty=quantity,product_price=productprice,subtotal=order_total,order=x)
    #             return HttpResponse("order completed successfully")
                
           
    #         else:
    #             return HttpResponse("order could not be completed :product required greater than stock")
    
    # elif request.user.is_authenticated :
    #     c=Product.objects.get(id=prid)
    #     print(c)
    #     return render(request,"checkout.html",{"product":c})
    
    # else:
    #     return redirect("register")