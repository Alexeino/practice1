from django.shortcuts import render
from rest_framework.generics import ListAPIView
from .models import *
from .serializers import *

# Create your views here.
class BooksAPI(ListAPIView):
    queryset = Book.objects.all().order_by('title')
    serializer_class = BookSerialzier