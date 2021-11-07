from rest_framework import serializers

from .models  import User,order
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model=User
        fields='__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model=order
        fields='__all__'