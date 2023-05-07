from rest_framework.serializers import Serializer, ModelSerializer
from .models import User
from django.contrib.auth.hashers import make_password



class UserRegisterSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email','password')
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate_password(self,password):
        password = make_password(password=password)
        return password
    
class UserSerializer(ModelSerializer):
    
    class Meta:
        model = User
        fields = ('email','first_name','last_name','role','is_active')
        
