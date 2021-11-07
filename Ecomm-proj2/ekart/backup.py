def viewcart(request):
    x=[]
    v=[]
    s=0
    if request.user.is_authenticated :
        k=request.user.id
        print(k)
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
        return render(request,"cart.html",{"product":x,"quantity":v,"price":s})
    else:
        return redirect("login")