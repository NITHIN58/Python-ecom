from rest_framework.response import Response
from rest_framework.decorators import api_view,APIView
from .models import Product
from .serializers import ProductSerializer

@api_view()
def  allProducts(request):
    ad=Product.objects.all()
    serializers=ProductSerializer(ad,many=True)
    return Response(serializers.data)

class productsclassview(APIView):
    def get(self,request):
        ad=Product.objects.all()
        print(ad)
        serializers=ProductSerializer(ad,many=True)
        return Response(serializers.data)