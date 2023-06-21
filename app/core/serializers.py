from rest_framework.serializers import ModelSerializer
from .models import *

class BookSerialzier(ModelSerializer):
    
    class Meta:
        model = Book
        fields = "__all__"