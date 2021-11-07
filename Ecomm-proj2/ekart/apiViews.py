from rest_framework.response import Response
from rest_framework.decorators import api_view,permission_classes
from .models import User,order
from .serializers import UserSerializer,OrderSerializer
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
#
@api_view(['POST'])
def signupView(request):
    if request.method=='POST':
        em=request.data.get('email')
        pw=request.data.get('password')
        usr=User.objects.create_user(email=em,password=pw)
        
        Token.objects.create(user=usr)
        t=Token.objects.get(user=usr).key

        return Response(data={'email':usr.email,'response':'Successfully registered a user','token':t})




@api_view()
@permission_classes([IsAuthenticated])
def showallusers(request):
    ad=User.objects.all()
    serializers=UserSerializer(ad,many=True)
    return Response(serializers.data)

@api_view()
@permission_classes([IsAuthenticated])
def showuserByemail(request):
    ad=User.objects.filter(email="nithinbiju58@gmail.com")
    serializers=UserSerializer(ad,many=True)
    return Response(serializers.data)

@api_view()
def showAllOrders(request):
    ad=order.objects.all()
    serializers=OrderSerializer(ad,many=True)
    return Response(serializers.data)

@api_view(['POST'])
def addcustomer(request):
    if request.method=='POST':
        email=request.data.get('email')
        username=request.data.get('username')
        password=request.data.get('password')
        postcode=request.data.get('postcode')
        city=request.data.get('city')
        phone=request.data.get('phone')
        k=User.objects.create_user(email=email,username=username,password=password,postcode=postcode,city=city,phone=phone)
        ad=User.objects.filter(email=k)
        serializer=UserSerializer(ad,many=True)
    return Response(serializer.data)

@api_view(['DELETE'])
def deleteuser(request,user):
    if request.method=="DELETE":
        c=User.objects.get(email=user)
        c.delete()
        return Response("deleted succeffully")


@api_view(['PUT'])
def updateuser(request,user):
    k=User.objects.filter(email=user).values()
    if request.method=="PUT":
        email=request.data.get('email')
        username=request.data.get('username')
        password=request.data.get('password')
        postcode=request.data.get('postcode')
        city=request.data.get('city')
        phone=request.data.get('phone')
        k.update(email=email,username=username,password=password,postcode=postcode,city=city,phone=phone)
        ad=User.objects.filter(email=k)
        serializer=UserSerializer(ad,many=True)
        return Response("updated succeffully")
        